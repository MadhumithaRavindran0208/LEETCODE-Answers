class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        t=float('inf')
        for i in range(len(landDuration)):
            land_end=landStartTime[i]+landDuration[i]
            for j in range(len(waterDuration)):
                water_end=waterStartTime[j]+waterDuration[j]
                finish_lw=max(waterStartTime[j],land_end)+waterDuration[j]
                finish_wl=max(landStartTime[i],water_end)+landDuration[i]
                t=min(t,finish_lw,finish_wl)
        return t