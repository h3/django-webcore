import warnings

try:
    import IPython
    try: # Legacy
        from IPython import Shell
        def brake():
            return Shell.IPShellEmbed()
    except: # New way
        def brake():
            return IPython.embed

except:
    def brake():
        warnings.warn("IPython shell doesn't seem to be installed.", ImportWarning)
        return lambda: ''
