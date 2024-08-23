import logging

import pandas as pd

logger = logging.getLogger(__name__)


def unify_contacts(data: list) -> list[list[str]]:
    """Unify duplicate contacts in a list of contacts.

    Args:
        data (list): A list of contacts, where each contact is a list.

    Returns:
        list: A list of unique contacts, where each contact is a list.

    Notes:
        - The function groups the contacts by the first two columns
          (name and surname) and aggregates the phone numbers and emails.
        - The function uses pandas DataFrame to perform the grouping
          and aggregation.
        - The function returns a list of unique contacts.
    """
    try:
        df = pd.DataFrame(data)
        df_grouped: pd.DataFrame = (
            df
            .groupby([0, 1], sort=False)
            .agg(
                {
                    2: lambda x: x.fillna('').values[0],
                    3: lambda x: x.fillna('').values[0],
                    4: lambda x: ''.join(x),
                    5: lambda x: x.fillna('').values[0],
                    6: lambda x: x.fillna('').values[0],
                }
            )
            .reset_index()
        )
        unique_contacts: list = df_grouped.values.tolist()
    except KeyError as e:
        logger.error(f"Ошибка ключа: {e}")
        return []
    except TypeError as e:
        logger.error(f"Ошибка типа: {e}")
        return []
    except ValueError as e:
        logger.error(f"Ошибка значения: {e}")
        return []

    return unique_contacts
