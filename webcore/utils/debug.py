import warnings

try:
    from IPython.Shell import IPShellEmbed
    def brake():
        return IPShellEmbed()
except:
    def brake():
        warnings.warn("IPython shell doesn't seem to be installed.", ImportWarning)
        return lambda x: x
