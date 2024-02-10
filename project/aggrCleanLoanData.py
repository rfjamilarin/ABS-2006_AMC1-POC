from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
import logging
from sqlConnection import sqlConnection
from sqlalchemy import MetaData, func

logger = logging.getLogger(__name__)

def calculate_sum(session, reflectedTable, column, label):
    try:
        inner_query = (
            session.query(
                reflectedTable.c.investor_loan_id,
                func.sum(column).label(label)
            )
            .group_by(reflectedTable.c.investor_loan_id)
            .subquery()
        )

        return session.query(func.sum(inner_query.columns[label])).scalar()

    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemy error in calculating sum: {str(e)}")
        return None

def aggrCleanLoanData(session, engine=None):
    data = {}

    try:
        metadata = MetaData()
        metadata.reflect(bind=engine, only=['loan_level_data'])
        reflectedTable = metadata.tables['loan_level_data']
                
        columnsToSum = [
            (reflectedTable.c.scheduled_principal, 'Scheduled Principal'),
            (reflectedTable.c.curtailments, 'Curtailments'),
            (reflectedTable.c.prepayment, 'Prepayments in Full'),
            ((reflectedTable.c.liquidation_principal - reflectedTable.c.principal_losses), 'Net Liquidation Proceeds'),
            (reflectedTable.c.repurchase_principal, 'Repurchase Principal'),
            (reflectedTable.c.other_principal_adjustments, 'Other Principal')
        ]

        for column, label in columnsToSum:
            total = calculate_sum(session, reflectedTable, column, label)
            if total is not None:
                data[label] = "{:,.2f}".format(total)
            else:
                data[label] = "N/A"

        totalFunds = sum(float(data[label].replace(',', '')) for label in data)
        data["Total Principal Funds Available"] = "{:,.2f}".format(totalFunds)

        logger.info("Aggregated loan data processed successfully.")

    except Exception as e:
        logger.error(f"Error in processing aggregated loan data: {str(e)}")

    finally:
        # Close the session
        session.close()

    return data
