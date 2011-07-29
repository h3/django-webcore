$(function(){

    $.frontadmin = (function(){
        var $self = this
        
        $self.initialized = false

        $self.bar = $('#frontadmin-bar-frame')
        $self.toolbars = $('.frontadmin-toolbar-frame')

        $self.button = {
            logout: '#frontadmin-btn-logout',
        }

        $self.events = {

            // Readjust bar & toolbars on window resize
            windowResized: function() {
                $self.toolbars.each(function(){
                    $(this).width($(this).parent().width())
                })
                var ww = $(document).width()
                var w =  parseInt(ww / 3)
                // Min width
                if (w < 300) { w = 300 }

                $self.bar.width(w)
                    .css('margin-left', ww / 2 - (w / 2))
            },

            onLogout: function(){
                $.get($(this).attr('href'), function(){
                    $self.toolbars.each(function(){
                        var wrapper = $(this).parents('.front-admin-block')
                        wrapper.find('.frontadmin-toolbar-frame').slideUp('fast', function(){
                                $(this).remove()
                            }).end().find('*').unwrap()
                        wrapper.remove()
                    })
                    $self.bar.slideDown('fast', function(){
                        $(this).remove()
                    })
                })
                return false
            }
        }

        $self.bindBarEvents = function() {
            var doc = $self.bar.contents()

            // Logout
            doc.find($self.button.logout).bind('click', $self.events.onLogout)
        }

        return {
            init: function() {
                $self.events.windowResized()
                $(window).resize($self.windowResized)
                // Little trick to load iframe content locally
                $self.bar.add($self.toolbars).each(function(){
                    $(this).contents().find('body').html($(this).text())
                })
                $self.bindBarEvents()
                $self.initialized = true
            }
        }
    })()

    $.frontadmin.init()

})
