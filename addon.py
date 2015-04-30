import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
rtmpurl = 'rtmp://aljazeeraflashlivefs.fplive.net:1935/aljazeeraflashlive-live/aljazeera_doc_high live=true'
 
xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(rtmpurl)