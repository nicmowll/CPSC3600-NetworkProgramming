# TODO: Import the config variable from the network_config module

class RoundTripLatencyCalculator:

    def __init__(self, config):
        # TODO: Perform any required initialization. Config should be a dictionary that contains
        #       all of the parameters necessary to calculate the latency for a given path through a network
        #       The config variable should be defined in a separate file named 'network_config.py'
        #       Delete "pass" once you have added code to this function.
        pass
        

    def calculate_total_RTT(self):
        # TODO: Compute the total round trip latency. You should use the below helper functions to break 
        #       the computation into its multiple component parts.
        #       Return the total round trip latency after computing it
        #       Remember that round trip latency includes the time to go there and back again
        #       Delete "pass" once you have added code to this function.
        pass
        

    def calculate_link_contribution(self, link_number):
        # TODO: Compute the total latency associated with a crossing a specific link one-way. 
        #       Hop number is the index of the link you are currently computing latency for
        #       Delete "pass" once you have added code to this function.
        pass
        

    def calculate_transmission_delay(self, link_number):
        # TODO: Compute the transmission delay associated with a given link 
        #       Link number is the index of the link you are currently computing latency for
        #       Delete "pass" once you have added code to this function.
        pass


    def calculate_propagation_delay(self, link_number):
        # TODO: Compute the propagation delay associated with a given link 
        #       Link number is the index of the link you are currently computing latency for
        #       Delete "pass" once you have added code to this function.
        pass


    def calculate_processing_delay(self, link_number):
        # TODO: Compute the processing delay associated with a given link 
        #       Link number is the index of the link you are currently computing latency for
        #       Delete "pass" once you have added code to this function.
        pass


    def calculate_queuing_delay(self, link_number):
        # TODO: Compute the queuing delay associated with a given link using the equations 
        #       delay = (0.1) / (1-delay_factor) - .1
        #       delay_factor = packet_length * average_packet_arrival_rate / bandwidth
        #       IMPORTANT: In real life, you can't predict exactly what the queueing delay will be. 
        #                  These equations roughly model what the size of the delay could be like in proportion
        #                  to how many packets are trying to move through a router at a given time 
        #       Link number is the index of the link you are currently computing latency for
        #       Delete "pass" once you have added code to this function.
        pass



# You do not need to change anything in the main method. It will not be called by the testing suite, so anything
# you implement here will not register when you submit your code. It is intended for your own personal testing only
if __name__ == "__main__":
    calc = RoundTripLatencyCalculator(config)

    latency = calc.calculate_total_RTT()
    print(latency)