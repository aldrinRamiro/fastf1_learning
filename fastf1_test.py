import fastf1 as fastf1
import pandas as pandas

#Enable cache
fastf1.Cache.enable_cache('cache')

#Get session
quali = fastf1.get_session(2021, 'Russia', 'Q') #Q = qualifying

laps = quali.load_laps(with_telemetry=True)

laps_nor = laps.pick_driver('NOR')
fastest_lap_nor = laps_nor.pick_fastest().LapTime

print ("Lando Norris' pole position lap was: "+ str(fastest_lap_nor))