class MapColoringCSP:
    def __init__(self, regions, neighbors, colors):
        self.regions = regions
        self.neighbors = neighbors
        self.colors = colors
        self.assignment = {}

    def is_consistent(self, region, color):
        for neighbor in self.neighbors[region]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def backtrack(self):
        if len(self.assignment) == len(self.regions):
            return self.assignment

        unassigned_regions = [region for region in self.regions if region not in self.assignment]

        first_unassigned_region = unassigned_regions[0]

        for color in self.colors:
            if self.is_consistent(first_unassigned_region, color):
                self.assignment[first_unassigned_region] = color

                if self.backtrack():
                    return self.assignment

                del self.assignment[first_unassigned_region]

        return None

def main():
    regions = ['A', 'B', 'C', 'D']
    neighbors = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    colors = ['Red', 'Green', 'Blue']

    csp = MapColoringCSP(regions, neighbors, colors)
    solution = csp.backtrack()

    if solution:
        print("Map Coloring Solution:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
