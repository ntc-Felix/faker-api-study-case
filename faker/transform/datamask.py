import pandas as pd
from typing import List

class MaskColumn:

    def __init__(self, df: pd.DataFrame()):
        """
        This class is a collection of operations for masking pandas
        Dataframes accordingly to the desired characteristics.
        Every method applies transformations at the record level

        Args:
            df (pd.DataFrame): Pandas DataFrame to be transformed
        """

        self.df = df

    def by_len(self, list_of_columns: List):
        """
        This method mask the row accordingly with its length.
        For example, the record with the string 'foo' will return '***'

        Args:
            list_of_columns (List): List of the columns to apply the function

        Returns:
            df: Pandas DataFrame with the transformed columns
        """

        df = self.df

        for col in list_of_columns:
            df[col] = df[col].astype(str).apply(lambda row: f"{len(row) * '*'}")

        return df

    def after_a_character(self, list_of_columns: List, character: str):
        """
        This method mask the row only after a certain parsed character.
        For example, the row with the value 'foo@email.com'
            will be transformed into 'foo@*********'(9*)

        Args:
            list_of_columns (List): List of the columns to apply the function
            character (str): String with the character that will be used as reference
                                to apply the method

        Returns:
            df: Pandas DataFrame with the transformed columns
        """

        df = self.df

        for col in list_of_columns:
            df[col] = df[col].astype(str).apply(
                                                lambda row:\
                                                    f"{row.split(character)[0]}{character}{len(row.split(character)[-1]) * '*'}"
                                                )

        return df
    
    def before_a_character(self, list_of_columns: List, character: str):
        """
        This method mask the row only after a certain parsed character.
        For example, the row with the value 'foo@email.com'
            will be transformed into '***@email.com'(3*)
        Args:
            list_of_columns (List): List of the columns to apply the function
            character (str): String with the character that will be used as reference
                                to apply the method

        Returns:
            df: Pandas DataFrame with the transformed columns
        """

        df = self.df

        for col in list_of_columns:

            df[col] = df[col].astype(str).apply(
                                                lambda row:\
                                                    f"{len(row.split(character)[0]) * '*'}{character}{row.split(character)[-1]}"
                                                )

        return df

    def keep_first(self, list_of_columns: List, length: int = 4):
        """
        This method masks the row by keeping a certain number of characters
            at the beginning of the string and replacing the others with '*'.
        For example, the word 'taxfix' will be transformed into 'taxf**'(4*)
        But the number of characters can be changed accordingly to the user's choice.
        For example, if the user specifies length=2 then 'taxfix' will be
            transformed into 'ta****' insted of 'taxf**'

        Args:
            list_of_columns (List): List of the columns to apply the function
            length (int, optional): Number of characters that you want to keep
                                    Default to 4.
        
        Returns:
            df: Pandas DataFrame with the transformed columns
        """

        df = self.df

        for col in list_of_columns:
            df[col] = df[col].astype(str).apply(lambda row: f"{row[:-length]}{length * '*'}")

        return df

    def keep_last(self, list_of_columns: List, length: int = 4):
        """
        This method masks the row by keeping a certain number of characters
            at the end of the string and replacing the others with '*'.
        For example, the word 'taxfix' will be transformed into '**xfix'(4*)
        But the number of characters can be changed accordingly to the user's choice.
        For example, if the user specifies length=2 then 'taxfix' will be
            transformed into '****ix' insted of '**xfix'
        Args:
            list_of_columns (List): List of the columns to apply the function
            length (int, optional): Number of characters that you want to keep
                                    Default to 4.

        Returns:
            df: Pandas DataFrame with the transformed columns
        """
        df = self.df

        for col in list_of_columns:
            df[col] = df[col].astype(str).apply(lambda row: f"{length * '*'}{row[length+1:]}")

        return df
