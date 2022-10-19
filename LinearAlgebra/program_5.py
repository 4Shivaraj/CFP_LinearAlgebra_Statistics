"""
    @Author: Shivaraj
    @Date: 18-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 18-10-2022
    @Title: Write a program to find inverse matrix of matrix X in problem 1
            X = [[12,7,3],
                [4 ,5,6],
                [7 ,8,9]]
"""

import sys

import numpy as np

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class MatrixComputations:

    def inverse_func(self, X):
        """
        Description:
             This function is used find inverse matrix of matrix X
        Parameter:
            X: The X is 3X3 size of matrix to be checked
        Return:
            Returns result
        """
        try:
            np_array = np.array(X)
            result = np.linalg.inv(np_array)
            return result

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    mat_obj = MatrixComputations()
    lg.info(f"After inversing the matrix: \n{mat_obj.inverse_func(X)}")
