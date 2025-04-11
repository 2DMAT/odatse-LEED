Input and output
================================

``odatse-LEED`` module is a ``Solver`` which calculates the Rocking curve from atomic positions etc., using ``SATLEED``, and returns the deviation from the experimental Rocking curve as :math:`f(x)`.

In this section, the input parameters, the input data, and the output data are explained.
The input parameters are taken from the ``solver`` entry of the ``Info`` class.
The parameters are specified in ``[solver]`` section when they are given from a TOML file.
If the parameters are given in the dictionay format, they should be prepared as a nested dict under the ``solver`` key.
In the following, the parameter items are described in the TOML format.

The input data consist of target reference data, and the bulk structure data.
The output data consist of files containing the result of optimization.
Their contents will be shown in this section.


Input parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Input parameters are specified in the ``solver`` section and the subsections (``config``, ``param``, and ``reference``).

- ``name``

  Format: string

  Description: The name of the direct problem solver. Optional.


- ``dimension``

  Format: integer

  Description: The number of parameters. If it is not specified, the dimension is taken from the [base] section.



[``config``] section
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``path_to_first_solver``

  Format: string

  Description: Path to the solver ``satl1.exe``. The default value is ``satl1.exe``.


- ``path_to_second_solver``

  Format: string

  Description: Path to the solver ``satl2.exe``. The default value is ``satl2.exe``.


- ``sigma_file_path``

  Format: string

  Description: Path to the experimental data file. The default value is ``exp.d``.


- ``remove_work_dir``

  Format: boolean

  Description: The output files of the solver program are stored in a directory ``LogXXXX_YYYY`` for each search point, in which ``XXXX`` denotes the step count and ``YYYY`` denotes the identifier such as replica number. When ``remove_work_dir`` is set to true, the directory is removed after the evaluation at the search point. The default value is false.


- ``use_tmpdir``

  Format: boolean

  Description: If it is true, the intermediate files are stored in a directory within /tmp or within the directory specified by the environment variable TMPDIR. The default value is false.


[``param``] section
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``string_list``

  Format: list of strings

  Description: List of keywords embedded in the input template files.


[``reference``] section
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``path_to_base_dir``

  Format: string

  Description: Path to the directory which stores ``exp.d``, ``rfac.d``, ``tleed4.i``, ``tleed5.i``.


- ``rfactor``

  Format: string or dictionary

  Description: Types of R-factor. The weighted average of multiple types of R-factors can be specified by a dictionary that relates the R-factor types and the relative weights.
  (For the latter, only the R-factor types r1 .. rpe are available.)

  The available types are described in the following section.
  The default value is ``rpe`` (Pendry R-factor).


- ``rescale``

  Format: boolean

  Description: If it is set to true, :math:`I_t` is rescaled in the R-factor calculation. The default value is false.


- ``smoothing factor``

  Format: float

  Description: The smoothing parameter for I-V curve data. If it is set to 0.0, the smoothing is not applied. The default value is 0.0.


- ``vi_value``

  Format: float

  Description: The imaginary part of the inner potential needed to calculate the Pendry R-factor. The parameter value can be explicitly specified by ``vi_value``, or it is obtained from the input file ``tleed5.i`` for SATLEED.


Types of R-factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The types of R-factors available for the ``rfactor`` parameter are listed as follows.

The notation is summarized:
:math:`\sum_b` denotes the sum over the beams.
:math:`\sideset{}{'}\sum_b = \sum_b w_b` denotes the sum over that beams that takes account of the relative weight of energy ranges :math:`w_b = {\int dE}/{\sum_b \int dE}`.
When ``rescale`` is set to true, :math:`c = {\int I_e dE}/{\int I_t dE}`, otherwise :math:`c=1`.

- rsq

  .. math::

     R = \sqrt{ \dfrac{\sum_b \int \left(I_e - I_t\right)^2 dE}{\sum_b \int I_e^{\,2} dE} }

- rsq_modified

  .. math::

     R = \sqrt{ \sideset{}{'}\sum_b \dfrac{\int \left(I_e - I_t\right)^2 dE}{\int I_e^{\,2} dE} }

- r1

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left| I_e - c I_t \right| dE}{\int I_e dE}

- r2

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left( I_e - c I_t \right)^2 dE}{\int I_e^{\,2} dE}

- rp1

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left| I_e^\prime - c I_t^\prime \right| dE}{\int \left|I_e^\prime\right| dE}

- rp2

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left( I_e^\prime - c I_t^\prime \right)^2 dE}{\int (I_e^\prime)^{2} dE}

- rpp1

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left| I_e^{\prime\prime} - c I_t^{\prime\prime} \right| dE}{\int \left|I_e^{\prime\prime}\right| dE}

- rpp2

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left( I_e^{\prime\prime} - c I_t^{\prime\prime} \right)^2 dE}{\int (I_e^{\prime\prime})^{2} dE}


- rrzj (reduced Zanazzi-Jona R-factor)

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{1}{0.027 \int I_e dE} \int \dfrac{\left| I_e^{\prime\prime} - c I_t^{\prime\prime} \right|\cdot\left| I_e^{\prime} - c I_t^{\prime} \right|}{\left|I_e^{\prime}\right| + {\rm max}\left|I_e^{\prime}\right|} dE

- rmzj (modified Zanazzi-Jona R-factor)

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{1}{\int I_e^{\prime\prime} dE} \int \dfrac{\left| I_e^{\prime\prime} - c I_t^{\prime\prime} \right|\cdot\left| I_e^{\prime} - c I_t^{\prime} \right|}{\left|I_e^{\prime}\right| + c\cdot{\rm max}\left|I_t^{\prime}\right|} dE

- rpe (Pendry R-factor)

  .. math::

     R = \sideset{}{'}\sum_b \dfrac{\int \left(Y_e - Y_t\right)^2 dE}{\int Y_e^{\,2} + Y_t^{\,2} dE}, \quad Y = \dfrac{L}{1 + V_{0i}^{\,2} L^2}, \quad L = {\tilde I}^\prime / {\tilde I}.

  In the Pendry R-factor, :math:`{\tilde I} = I_t + \kappa {\langle I \rangle}`, where :math:`\kappa` is the parameter denoted by ``PERSH``, and it is set to 0.05.
  :math:`{\langle I \rangle}` is the average over the peaks of :math:`I`.
  :math:`V_{0i}` denotes the imaginary part of the inner potential.

  N.B. when RPE (the Pendry R-factor) is chosen in rfac.d for the R-factor (i.e. WR(10) is set to 1), the output of I-V curves contains :math:`{\tilde I}` instead of :math:`I`. Therefore, WR(10) must be set to 0 except when ``satleed`` is chosen for ``rfactor`` type.

- satleed

  The value of R-factor is taken from the output (search.s) of satl2.exe.


Reference file for Solver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target reference file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The file containing the data to be targeted to fit. Edit ``tleed4.i`` and ``tleed5.i`` in ``path_to_base_dir`` in the [``reference``] section.

The parameter values to be optimized are replaced by the keywords that depend on the types of parameters:
The coordinates or the deviations of the coordinates are denoted by strings starting from ``opt``.
The inner potential is denoted by strings starting from ``IP``.
The Debye temperatures are denoted by strings starting from ``debye``.
The keywords are listed in the parameter ``solver.param.string_list`` in the input file.
The number and the order of the keywords should be identical to those of the list of variables to optimize.

The keywords should be embedded in the templates according to the format of the parameters.
In the following example, the parameter values corresponding to ``opt000`` and ``opt001`` (e.g. 0.23) are formatted by the format style ``(F7.4)`` (7 letters in total with 4 digits below the floating point) such as ``␣0.2300``.

Note that if IFLAG and LSFLAG are not set to 0, the satleed side is also optimized.

An example file is shown below.

.. code-block::

    1  0  0                          IPR ISTART LRFLAG
    1 10  0.02  0.2                  NSYM  NSYMS ASTEP VSTEP
    5  1  2  2                       NT0  NSET LSMAX LLCUT
    5                                NINSET
    1.0000 0.0000                  1      PQEX
    1.0000 2.0000                  2      PQEX
    1.0000 1.0000                  3      PQEX
    2.0000 2.0000                  4      PQEX
    2.0000 0.0000                  5      PQEX
    3                                 NDIM
   opt000 0.0000 0.0000  0           DISP(1,j)  j=1,3
    0.0000opt001 0.0000  0           DISP(2,j)  j=1,3
    0.0000 0.0000 0.0000  1           DISP(3,j)  j=1,3
    0.0000 0.0000 0.0000  0           DISP(4,j)  j=1,3
    0.0000  0                         DVOPT  LSFLAG
    3  0  0                           MFLAG NGRID NIV
    ...

Output file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``leed``, the output files are stored in the subfolder ``LogXXXX_YYYY`` for each parameter value that is created in the folder with the rank number within the ``output_dir``.
Here, ``XXXX`` denotes the step count, and ``YYYY`` denotes the identifier such as the replica number.
