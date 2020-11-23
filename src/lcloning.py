# This script generates an edgelist based on the L-cloning algorithm proposed by
#
#   Network cloning unfolds the effect of clustering on dynamical processes
#   Ali Faqeeh, Sergey Melnik, and James P. Gleeson
#   Phys. Rev. E 91:052807 (2015)
#   doi: 10.1103/PhysRevE.91.052807
#
#  Usage: python3 lcloning.py [original edgelist] [cloned_edgelist] [nb copies]
#
#  Author:  Antoine Allard
#  WWW:     antoineallard.info
#  Date:    December 2017
#
#
#  Copyright (C) 2019 Antoine Allard
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Packages
import random as rnd
import numpy as np
import sys

# Filenames.
original_edgelist_filename = sys.argv[1]
l_cloned_edgelist_filename = sys.argv[2]

# Number of times the edgelist must be duplicated.
nb_copies = int(sys.argv[3])

# Array to swap edges between "layers".
shuffled_layer_id = [int(i) for i in np.arange(nb_copies)]

# Make the replication by appending a number to vertices's name.
with open(original_edgelist_filename, "r") as input_file:
    with open(l_cloned_edgelist_filename, "w") as output_file:
        # Header of the file.
        output_file.write("#")
        output_file.write("{:>19}".format("Vertex1") + " ")
        output_file.write("{:>20}".format("Vertex2") + " \n")
        # Duplicate each edge by shuffling between "layers".
        for line in input_file:
            # Gets the vertices of the edge.
            sline = line.split()
            if sline[0][0] != "#":
                # Shuffles the layers.
                rnd.shuffle(shuffled_layer_id)
                # Write the resulting edges into the output file.
                for n in range(nb_copies):
                    output_file.write("{:>20}".format(sline[0] + "_" +
                                      str(n)) + " ")
                    output_file.write("{:>20}".format(sline[1] + "_" +
                                      str(shuffled_layer_id[n])) + " \n")
