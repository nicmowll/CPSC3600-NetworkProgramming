# TODO: Define a variable named 'config' containing the following key-value pairs. These variables
#       store all of the information you need to compute a packet's round trip latency through a 
#       given network.
#       
#       * 'packet_length' stores the length of the packet in bytes
#       * 'num_links' stores the number of unique links the packet will pass through. As an example, 
#          num_links would be 3 in the below network:
#          [Host A] <----link----> [Router 1] <----link----> [Router 2] <----link----> [Host B]
#       * 'bandwidths' stores a list of length 'num_links'. Each entry in the list corresponds to 
#          the bandwidth of the associated link
#       * 'distances' stores a list of length 'num_links'. Each entry in the list corresponds to 
#          the distance of the associated link
#       * 'transmission_speeds' stores a list of length 'num_links'. Each entry in the list 
#          corresponds to the transmission speed of the associated link
#       * 'processing_delays' stores a list of length 'num_links'. Each entry in the list corresponds 
#          to the processing delay incured by the associated link
#       * 'average_packet_arrival_rates' stores a list of length 'num_links'. Each entry in the list 
#          corresponds to the average rate packets are arriving over the associated link
#
#       Assume that distances are represented in meters and memory sizes are in bits. Your code should 
#       return RTT in seconds. You do not need to do any unit conversions in your code.

config = {}