# Test_singulars
A set of python programs for computing matrices and a unit test to check if matrices are singular.
### What is a singular matrice:

A rectangular matrix of values  is said to be singular when the elements of a column (or a row) of the matrix are the linear combination of the elements of one or several other columns (or rows) of this matrix. For example, if the elements of a column of a matrix are 1, -1, 0, and the elements of another column of this matrix are 2, -2, 0, the matrix is then singular since the value of the elements in the first column is equal to each of the corresponding elements in the second column. We also talk about the multicollinearity problem, since one or more columns are linearly dependent on the others.<br>
### It has the following features:
- It is not possible to compute the inverse of singular matrices, but it is on the other hand possible to compute generalized inverses (in fact, an infinity) for all singular matrices.
- The determinant is always equal to zero<br>
<br>

`!!This program relies on numpy so please be sure to have it in your python packages and an asciinema can be found on`![this]( https://asciinema.org/a/xIMSZVsrox7k7uWrwZi2fbf8o) link
<br><br><br><br>
Made by `Shadowblade` During `GCI 2019`, Open source
