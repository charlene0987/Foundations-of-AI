from constraint import Problem

problem = Problem()

"""map of Australia"""
# Define the 5 regions
regions = ['WA', 'NT', 'SA', 'Q', 'NSW']
# Define the available colors 
colors = ['Red', 'Blue', 'Green']

problem.addVariables(regions, colors)

# Define Adjacency Constraints (Edges)
# No two touching regions can have the same color
adjacencies = [
    ('WA', 'NT'), ('WA', 'SA'),
    ('NT', 'SA'), ('NT', 'Q'),
    ('SA', 'Q'), ('SA', 'NSW'),
    ('Q', 'NSW')
]

for region1, region2 in adjacencies:
    problem.addConstraint(lambda r1, r2: r1 != r2, (region1, region2))

# Solve
solution = problem.getSolution()
print("Australia Coloring Solution:", solution)

"""map of Nairobi"""
problem_nairobi = Problem()

sub_counties = [
    'Westlands', 'DagNorth', 'DagSouth', 'Langata', 'Kibra', 
    'Roysambu', 'Kasarani', 'Ruaraka', 'EmbSouth', 'EmbNorth', 
    'EmbCentral', 'EmbEast', 'EmbWest', 'Makadara', 'Kamukunji', 
    'Starehe', 'Mathare'
]

# Least possible colors for a complex planar map is 4
colors = ['Color1', 'Color2', 'Color3', 'Color4']

problem_nairobi.addVariables(sub_counties, colors)

# Example of key adjacencies in Nairobi
# (In a full program, all 17 borders would be mapped here)
nairobi_adjacencies = [
    ('Westlands', 'DagNorth'), ('Westlands', 'Starehe'),
    ('DagNorth', 'DagSouth'), ('DagNorth', 'Kibra'),
    ('Langata', 'Kibra'), ('Langata', 'DagSouth'),
    ('Starehe', 'Mathare'), ('Starehe', 'Kamukunji'),
    ('Mathare', 'Ruaraka'), ('EmbakasiEast', 'EmbakasiCentral')
]

for sc1, sc2 in nairobi_adjacencies:
    problem_nairobi.addConstraint(lambda a, b: a != b, (sc1, sc2))

solution_nairobi = problem_nairobi.getSolution()
print("Nairobi Least-Color Solution:", solution_nairobi)