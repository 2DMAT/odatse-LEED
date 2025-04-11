Installation of odatse-LEED
================================

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Python3 (>=3.9)

- The following Python packages are required.

  - numpy >= 1.14
  - pydantic >= 2.0
  - fortranformat
  - ODAT-SE >= 3.0

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

     .. note::
        For Python versions below 3.7, you will get the following error. Please use Python 3.9 or higher for this package.

        .. code-block:: bash

           Directory '.' is not installable. File 'setup.py' not found.

     If you run the following command instead, optional packages will also be installed at the same time.

     .. code-block:: bash

	$ python3 -m pip install .[all]

2. Install odatse-LEED

   - From source files:

     The source files of odatse-LEED are available from the GitHub repository. After obtaining the source files, install odatse-LEED using ``pip`` command as follows:

     .. code-block:: bash

        $ cd ../
        $ git clone https://github.com/2DMAT/odatse-LEED.git
        $ cd odatse-LEED
        $ python3 -m pip install .

     You may add ``--user`` option to install the package locally (in ``$HOME/.local``).
     Then, the library of odatse-LEED and the command ``odatse-LEED`` wil be installed.

3. Install SATLEED

   - The source archive is available from the following URL.

     .. code-block:: bash

         http://www.icts.hkbu.edu.hk/VanHove_files/leed/leedsatl.zip

     Unpack the source package, and compile the source.

   - ``SATLEED`` requires modifying source code parameters according to the details of the system you want to calculate.
     The source files of odatse-LEED include ``leedsatl.patch`` for modifying the source code and ``setup.sh`` script for automatic compilation in the ``sample/satleed`` directory. 
     You can use these files to install SATLEED.

     .. code-block:: bash

         $ cd odatse-LEED/sample/satleed
         $ sh ./setup.sh

     By running ``setup.sh``, the executable files ``satl1.exe`` and ``satl2.exe`` will be generated in the current directory.

     You may edit ``setup.sh`` to use other compilers or to apply different compiler options.


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
