import asyncio

from competition import race_gui
from racer_types.Animal import Animal


class Turtle(Animal):
    async def pass_out(self, progress):
        progress += self.steps_before_pass_out
        await race_gui.racer_progress_print(self, progress)
        await race_gui.passed_out_print(self)
        await asyncio.sleep(self.passed_out_time)
        difference = self.steps_per_interval - self.steps_before_pass_out
        progress += difference
        return progress
