
try:
    from IPython.Shell import IPShellEmbed
    def brake():
        return IPShellEmbed()
except:
    def brake():
        return lambda x: x
