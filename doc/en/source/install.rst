Installation of odatse-LEED
================================

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Python3 (>=3.6.8)

  - The following Python packages are required.

    - tomli >= 1.2
    - numpy >= 1.14

  - ODAT-SE version 3.0 and later

  - SATLEED

    - A Fortran compiler is required for compilation.


How to download and install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install ODAT-SE

   - From source files:

     Download source files of ODAT-SE from the repository as follows:

     .. code-block:: bash

	$ git clone https://github.com/issp-center-dev/ODAT-SE.git

     Install ODAT-SE using ``pip`` command:

     .. code-block:: bash

	$ cd ODAT-SE
	$ python3 -m pip install .

     You may add ``--user`` option to install ODAT-SE locally (in ``$HOME/.local``).

     If you run the following command instead, optional packages will also be installed at the same time.

     .. code-block:: bash

	$ python3 -m pip install .[all]

2. Install SATLEED

   - The source archive is available from the following URL.

     .. code-block:: bash

        $ wget http://www.icts.hkbu.edu.hk/VanHove_files/leed/leedsatl.zip

   - Unpack the source package, and compile the source.

     It is necessary to modify parameters in the source files of ``SATLEED`` according to the details of the system under consideration.
     For the present tutorial, a script ``setup.sh`` is prepared that automatically modifies the parameters and compile the source files.

     .. code-block:: bash

	$ cd sample/mapper
	$ sh ./setup.sh

     By running ``setup.sh``, the executable files ``satl1.exe`` and ``satl2.exe`` will be generated in ``leedsatl`` directory.
     
3. Install odatse-LEED

   - From source files:

     The source files of odatse-LEED are available from the GitHub repository. After obtaining the source files, install odatse-LEED using ``pip`` command as follows:

     .. code-block:: bash

	$ git clone https://github.com/2DMAT/odatse-LEED.git
	$ cd ODAT-SE
	$ python3 -m pip install .

     You may add ``--user`` option to install the package locally (in ``$HOME/.local``).

     Then, the library of odatse-LEED and the command ``odatse-LEED`` wil be installed.


How to run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In ODAT-SE, the analysis is done by using a predefined optimization algorithm and a direct problem solver.
There are two ways to do analyses of LEED:

1. Use odatse-LEED program included in this package to perform analyses.
   The users prepare an input parameter file in TOML format, and run command with it.
   The type of the inverse problem algorithms can be chosen by the parameter.

2. Write a program for the analysis with odatse-LEED library and ODAT-SE framework.
   The type of the inverse problem algorithms can be chosen by importing the appropriate module.
   A flexible use would be possible, for example, to include data generation within the program.
   
The types of parameters and the instruction to use the library will be given in the subsequent sections.


How to uninstall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In order to uninstall odatse-LEED and ODAT-SE modules, type the following commands:

.. code-block:: bash

   $ python3 -m pip uninstall odatse-LEED ODAT-SE
