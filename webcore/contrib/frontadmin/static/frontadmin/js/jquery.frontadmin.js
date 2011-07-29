$(function(){

    $.frontadmin = (function(){
        var $self = this
        
        $self.states = {
            initialized: false,
            toolbars_visibles: false
        }

        $self.bar = $('#frontadmin-bar-frame')
        $self.toolbars = $('.frontadmin-toolbar-frame')

        $self.buttons = {
            logout: '#frontadmin-btn-logout',
            toggle: '#frontadmin-btn-toggle',
        }

        $self.cookie = function(k, v) {
            if (v) { return $.cookie(k, v, {path: '/'}) }
            else   { return $.cookie(k,    {path: '/'}) }
        }

        // frontadmin toolbar initial state
        if ($self.cookie('frontadmin_toolbars_visibles') == null) { 
            // Cookie does not exist, set it and show the toolbar by default
            $self.cookie('frontadmin_toolbars_visibles', 'true')
            $self.states.toolbars_visibles = true
        }
        $('html')[($self.toolbars_visibles == true && 'addClass' || 'removeClass')]('frontadmin-show-toolbars')

        $self.events = {

            // Readjust bar & toolbars on window resize
            onWindowResize: function(e) {
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
            
            // Log the user out and hide frontadmin
            onLogout: function(e){
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
            },                

            // toggle frontadmin ui
            onToggleToolbar: function(e){
                $('html').toggleClass('frontadmin-show-toolbars')
                $self.cookie('frontadmin_toolbars_visibles', $('html').hasClass('frontadmin-show-toolbars') && true || false)
                return false;
            }
        }

        $self.bindBarEvents = function() {
            var doc = $self.bar.contents()
            doc.find($self.buttons.logout).bind('click.frontadmin', $self.events.onLogout).end()
               .find($self.buttons.toggle).bind('click.frontadmin', $self.events.onToggleToolbar).end()

        }

        return {
            init: function() {
                $self.events.onWindowResize()
                $(window).resize($self.events.onWindowResize)

                // Little trick to load iframe content locally
                $self.bar.add($self.toolbars).each(function(){
                    $(this).contents().find('body').html($(this).text())
                })
                $self.bindBarEvents()
                $self.states.initialized = true
            }
        }
    })()

    $.frontadmin.init()

})
