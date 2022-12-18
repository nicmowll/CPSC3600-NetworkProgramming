from layer_header import LayerHeader
from struct import pack, unpack

class IPv4Header(LayerHeader):
    def __init__(self, pkt):
        # TODO: Replace the value of header_length with the length of an Ethernet header
        header_length = 20
        
        # TODO: If this header can be variable length, you will need to update the contents of 
        #       self.header_bytes once you know the full length of the header in order to ensure
        #       that all of the bytes associated with this header are saved. 
        #       You can leave it as is for now.
        self.header_bytes = pkt[:header_length]

        self.version = None
        self.IHL = None
        self.TOS = None
        self.total_length = None
        self.identification = None
        self.flags = None
        self.fragment_offset = None
        self.TTL = None
        self.transport_protocol = None
        self.checksum = None
        self.source_addr = None
        self.dest_addr = None
        self.options_bytes = None

        # TODO: Unpack the header and assign the values to the above variables

        ip4_header = unpack('!BBHHHBBHII', self.header_bytes)
        self.version = ip4_header[0] >> 4
        self.IHL = ip4_header[0] & 0xf
        self.TOS = ip4_header[1]
        self.total_length = ip4_header[2]
        self.identification = ip4_header[3]
        self.flags = ip4_header[4] >> 3
        self.fragment_offset = ip4_header[4] & 8191
        self.TTL = ip4_header[5]
        self.transport_protocol = ip4_header[6]
        self.checksum = ip4_header[7]
        self.source_addr = ip4_header[8]
        self.dest_addr = ip4_header[9]

        # TODO: You do not need to unpack any options, if they are present in the header. However, if options 
        #       are present, store the bytes associated with them in self.options_bytes.
        
        if(self.IHL > 5):
            options_len = self.total_length - header_length
            self.options_bytes = unpack('!H' + str(options_len) + 's', pkt[header_length:header_length + options_len])
    
    
    def protocol(self):
        return "IPv4"

    def header_bytes(self):
        return self.header_bytes

    def print_header(self):
        print("")
        print("IPv4 HEADER: ")
        line_width = (96+4)

        ####################################################################
        # Print first line
        print("-"*line_width)
        
        # Compose the contents of the first row of the header
        version_str = "VERSION: " + hex(self.version)
        white_space = (16 - len(version_str))//2
        first_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        ihl_str = "IHL: " + hex(self.IHL)
        white_space = (16 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        tos_str = "TOS: " + hex(self.TOS)
        white_space = (16 - len(tos_str))//2
        first_row_str += " "*white_space + tos_str + " "*white_space + "|"

        length_str = "LENGTH: " + hex(self.total_length)
        white_space = (47 - len(length_str))//2
        first_row_str += " "*white_space + length_str + " "*white_space + "|"

        # Print the first row of the header
        print(first_row_str)
        


        ####################################################################
        # Print a line divider
        print("-"*line_width)

        # Compose the contents of the second row of the header
        version_str = "IDENT: " + hex(self.identification)
        white_space = (48 - len(version_str))//2
        second_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        tos_str = "FLAGS: " + bin(self.flags)
        white_space = (16 - len(tos_str))//2
        second_row_str += " "*white_space + tos_str + " "*white_space + "|"

        length_str = "FRAG OFFSET: " + str(self.fragment_offset)
        white_space = (32 - len(length_str))//2
        second_row_str += " "*white_space + length_str + " "*white_space + "|"

        # Print the second line of the header
        print(second_row_str)


        ####################################################################
        # Print a line divider
        print("-"*line_width)
      
        # Compose the contents of the second row of the header
        version_str = "TTL: " + str(self.TTL)
        white_space = (24 - len(version_str))//2
        third_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        tos_str = "Protocol: " + hex(self.transport_protocol)
        white_space = (24 - len(tos_str))//2
        third_row_str += " "*white_space + tos_str + " "*white_space + "|"

        length_str = "CKSUM: " + hex(self.checksum)
        white_space = (48 - len(length_str))//2
        third_row_str += " "*white_space + length_str + " "*white_space + "|"

        # Print the second line of the header
        print(third_row_str)



        ####################################################################
        # Print a line divider
        print("-"*line_width)
      
        # Compose the contents of the second row of the header
        version_str = "SOURCE ADDR: " + self.format_IPv4_addr(self.source_addr)
        white_space = (98 - len(version_str))//2
        third_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        # Print the fourth line of the header
        print(third_row_str)



        ####################################################################
        # Print a line divider
        print("-"*line_width)
      
        # Compose the contents of the second row of the header
        version_str = "DEST ADDR: " + self.format_IPv4_addr(self.dest_addr)
        white_space = (98 - len(version_str))//2
        third_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        # Print the fourth line of the header
        print(third_row_str)



        ####################################################################
        # Print a line divider
        print("-"*line_width)

        return super().print_header()