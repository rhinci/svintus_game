import time

class RunStatistics:
    def __init__(self):
        self.reset_stats()
        self.run_start_time = None
    #обновление статистики
    def reset_stats(self):
        self.current_stats = {
            "1. Kills": 0,
            "2. Time played": int(0),
            "3. Crystals collected": 0,
            "4. Damage taken": 0,
            "5. Damage dealt": 0,
            "6. Bullets used": 0,
        }
    #старт работы статистики
    def start_run(self):
        self.reset_stats()
        self.run_start_time = time.time()
    #окончание работы статистики
    def end_run(self):
        if self.run_start_time is not None:
            self.current_stats["2. Time played"] = time.time() - self.run_start_time
            self.run_start_time = None
            return self.current_stats.copy()
        return None
    #увеличение определенной статистики
    def increment_stat(self, stat_name, amount=1):
        if stat_name in self.current_stats:
            self.current_stats[stat_name] += amount
    #обновление статистики
    def update_stat(self, stat_name, value):
        if stat_name in self.current_stats:
            self.current_stats[stat_name] = value
    #получение статистики
    def get_stats(self):
        stats = self.current_stats.copy()
        if "2. Time played" in stats:
            stats["2. Time played"] = round(stats["2. Time played"], 1)
        return stats

run_stats = RunStatistics()
