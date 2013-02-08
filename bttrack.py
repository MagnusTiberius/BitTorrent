#!/usr/bin/env python

# Written by Bram Cohen
# see LICENSE.txt for license information

PROFILE = 0
    
import sys
from BitTornado.BT1.track import track

if __name__ == '__main__':
    if PROFILE:
        import profile, pstats
        from time import strftime
        p = profile.Profile()
        p.runcall(track, sys.argv[1:])
        log = open('profile_data.'+strftime('%y%m%d%H%M%S')+'.txt','a')
        normalstdout = sys.stdout
        sys.stdout = log
#        pstats.Stats(p).strip_dirs().sort_stats('cumulative').print_stats()
        pstats.Stats(p).strip_dirs().sort_stats('time').print_stats()
        sys.stdout = normalstdout
    else:
        track(sys.argv[1:])
