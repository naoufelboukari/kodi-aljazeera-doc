import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
rtmpurl = 'http://46.245.160.224/mekke/mekke/chunklist_w581447799.m3u8 live=true'
 
xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(rtmpurl)