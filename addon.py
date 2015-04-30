import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
rtmpurl = 'http://aljazeera-doc-apple-live.adaptive.level3.net/apple/aljazeera/hq-doc/800kStream.m3u8 live=true'
 
xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(rtmpurl)