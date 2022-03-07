import csv
from Models import utils
from pandas import period_range
from Engine.ExtractionPeriodBasicScheduleResult import ExtractionPeriodBasicScheduleResult


class ProductionPlanResult:
    units: list[ExtractionPeriodBasicScheduleResult]

    def __init__(self, units: list[ExtractionPeriodBasicScheduleResult]):
        self.units = units
        utils.get_column_average()

    def dump_units(self, filepath: str):
        """Dump all units

        Args:
            filepath (str): csv filepath
        """
        
        lines : list[str] = []
        
        header = "Period,Subscript I, Subscript J,Extracted Tonnage, From Meters,To Meters,Is Depleted,Tonnage Availble, Target Tonnage, Accomplished\n"
        lines.append(header)
        for unit in self.units:
            line = f"{unit.period_id},{unit.footprint_subscripts.i},{unit.footprint_subscripts.j},"
            line = line + f"{unit.extracted_tonnage},{unit.from_meters},{unit.to_meters},{unit.is_depleted},"
            line = line + f"{unit.tonnage_available},{unit.target_tonnage},{unit.was_target_accomplished}\n"
            lines.append(line)
         
        with open(filepath,'w+') as write_file:
            write_file.writelines(lines)
