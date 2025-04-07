# odatse-LEED -- Low Energy Electron Diffraction solver module for ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.

import sys

if len(sys.argv) < 4:
    print("usage: {} tol file1 file2".format(sys.argv[0]))
    sys.exit(0)

tol = float(sys.argv[1])
file_a = sys.argv[2]
file_b = sys.argv[3]

err = 0
with open(file_a, "r") as fa, open(file_b, "r") as fb:
    for idx, (ta, tb) in enumerate(zip(fa, fb)):
        vas = ta.split()
        vbs = tb.split()
        if len(vas) != len(vbs):
            print("DIFF: line {}: number of keywords differ: {} {}".format(idx, len(vas), len(vbs)))
            err += 1
            continue
        for id, (va, vb) in enumerate(zip(vas, vbs)):
            # literally equal
            if va == vb:
                continue
            # try compare as integers
            try:
                iva = int(va)
                ivb = int(vb)
                if iva == ivb:
                    continue
            except ValueError:
                pass
            # try compare as floating point numbers
            try:
                fva = float(va)
                fvb = float(vb)
                if abs(fva) < tol and abs(fvb) < tol:
                    r = abs(fva - fvb)
                else:
                    r = abs(fva - fvb) / (abs(fva) + abs(fvb))
                if r < tol:
                    continue
            except ValueError:
                pass
            # different anyway
            err += 1
            print("DIFF: line {}, item {}: \"{}\" \"{}\"".format(idx, id, va, vb))

if err > 0:
    print("comparison failed (err={}, tolerance={:.4e})".format(err,tol))
    sys.exit(1)

sys.exit(0)
