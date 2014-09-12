from pyshark import LiveCapture


class RemoteCapture(LiveCapture):
    """
    A capture which is performed on a remote machine which has an rpcapd 
    service running.
    """

    def __init__(self, remote_host, remote_interface, remote_port=2002, 
                 bpf_filter=None, only_summaries=False, decryption_key=None, 
                 encryption_type='wpa-pwd'):
        """
        Creates a new remote capture which will connect to a remote machine 
        which is running rpcapd. Use the sniff() method
        to get packets.
        Note: The remote machine should have rpcapd running in null 
        authentication mode (-n). Be warned that the traffic is unencrypted!

        :param remote_host: The remote host to capture on (IP or hostname). 
        Should be running rpcapd.
        :param remote_interface: The remote interface on the remote machine 
        to capture on. Note that on windows it is
        not the device display name but the true interface name 
        (i.e. \\Device\\NPF_..).
        :param remote_port: The remote port the rpcapd service is listening on
        :param bpf_filter: A BPF (tcpdump) filter to apply on the cap before 
        reading.
        :param only_summaries: Only produce packet summaries, much faster but 
        includes very little information
        """
        interface = 'rpcap://%s:%d/%s' % (remote_host, remote_port, 
                                          remote_interface)
        super(RemoteCapture, self).__init__(interface, bpf_filter=bpf_filter, 
                                            only_summaries=Falser,
                                            decryption_key=decryption_key, 
                                            encryption_type=encryption_type)
