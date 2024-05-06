import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import math

def plot_route(G, origin_node, destination_node, route):
    """
    Function to plot the route on a map with highlighted start and end points.
    
    """
    # Color the nodes
    node_colors = ['#FFFFFF' for node in G.nodes()]
    node_sizes = [15 if node not in [origin_node, destination_node] else 100 for node in G.nodes()]
    
    # Plot the graph
    fig, ax = ox.plot_graph(G, node_color=node_colors, node_size=node_sizes, bgcolor='k', show=False, close=False)

    # Plot the route if it exists
    if route:
        ox.plot_graph_route(G, route, route_color='red', route_linewidth=6, orig_dest_node_color='blue', orig_dest_node_size=100, ax=ax)
    
    # Get node positions directly from graph nodes' data
    start_pos = G.nodes[origin_node]['x'], G.nodes[origin_node]['y']
    end_pos = G.nodes[destination_node]['x'], G.nodes[destination_node]['y']

    # Add labels for the start and end nodes with some offset for visibility
    ax.text(start_pos[0], start_pos[1], 'Start', color='white', fontsize=12, bbox=dict(facecolor='white', alpha=0.8), horizontalalignment='left')
    ax.text(end_pos[0], end_pos[1], 'End', color='white', fontsize=12, bbox=dict(facecolor='white', alpha=0.8), horizontalalignment='right')

    # Save the figure before showing it
    #plt.savefig('/Users/shashwatsingh/Documents/GitHub/FocusRide/sampleroute.png')
    plt.show()

def main():
    
    route_optimisation("Empire State Building, New York", "Intrepid Museum, New York")

def route_optimisation(start_location_text, end_location_text):
    '''
        Arguments:
        start_location_text: string:  "Starting point for route"
        end_location_text: string:  "Ending point for route"

        This function uses osmnx and networkx library to get the shortest route between 2 points.
    '''
    
    # Geocode locations
    start_point = ox.geocode(start_location_text)
    end_point = ox.geocode(end_location_text)


    rounded_start_point = (round(start_point[0], 4), round(start_point[1], 4))
    print("Rounded coordinates:", rounded_start_point)

    rounded_end_point = (round(end_point[0], 4), round(end_point[1], 4))
    print("Rounded coordinates:", rounded_end_point)
    
    #Get the haversine distance to approximate the size of the map 
    dist=haversine_distance(rounded_start_point,rounded_end_point)
    print("distance- "+str(dist))
    dist=(dist/2)+500

    radius=min(dist,5000)


    # Create graph from point with a specified distance
    G = ox.graph_from_point(start_point, dist=radius, network_type='drive')

    # Find the nearest nodes to two points (start and end)
    origin_node = ox.distance.nearest_nodes(G, X=rounded_start_point[1], Y=rounded_start_point[0])
    destination_node = ox.distance.nearest_nodes(G, X=rounded_end_point[1], Y=rounded_end_point[0])


    # Find the shortest path using Dijkstra's Algorithm
    try:
        route = nx.shortest_path(G, origin_node, destination_node, weight='length')
    except nx.NetworkXNoPath:
        print("No path between the chosen nodes.")
        route = []

    # Plot the route
    plot_route(G, origin_node, destination_node, route)

    # Display route length
    if route:
        route_length = sum(ox.utils_graph.get_route_edge_attributes(G, route, 'length'))
        print(f"Route length: {route_length} meters")
    else:
        print("No route found to display.")

# Calculate distance to plot the map according to the distance between start and end points    
def haversine_distance(coord1, coord2):
    '''
    Calculates the distance between 2 points based on coordinates
    '''
    # Radius of Earth in kilometers
    R = 6371.0

    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c * 1000  # Convert to meters
    return distance

if __name__ == "__main__":
    main()
    
