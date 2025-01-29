from datetime import datetime, timedelta
import math

class ThaiLunarCalendar:
    # ค่าคงที่
    EPOCH = datetime(1900, 1, 1)
    LUNAR_CYCLE_DAYS = 29.53059  # จำนวนวันในรอบจันทรคติ

    @staticmethod
    def get_lunar_date(date: datetime):
        # คำนวณจำนวนวันตั้งแต่ Epoch
        days_since_epoch = (date - ThaiLunarCalendar.EPOCH).days

        # คำนวณวันที่ในรอบจันทรคติ
        lunar_day = (days_since_epoch % ThaiLunarCalendar.LUNAR_CYCLE_DAYS) + 1

        # คำนวณขึ้น/แรม และค่ำ
        day_of_month = round(lunar_day) if lunar_day > 15.8714  else math.floor(lunar_day)
        
        if day_of_month <= 15:
            phase = "ขึ้น"
            day_count = day_of_month
        elif day_of_month <= 30:
            phase = "แรม"
            day_count = day_of_month - 15
        elif day_of_month <= 45:
            phase = "ขึ้น"
            day_count = day_of_month - 30
        else:
            phase = "แรม"
            day_count = day_of_month - 45

        # ตรวจสอบว่าเป็นวันพระหรือไม่
        is_wan_phra = (phase == "ขึ้น" and day_count in {8, 15}) or \
                      (phase == "แรม" and day_count in {8, 14, 15})

        thai_month = ThaiLunarCalendar.get_thai_month(date, phase, day_count)
        # คืนค่าผลลัพธ์
        return f"{phase} {int(day_count)} ค่ำ เดือน {int(thai_month)}", is_wan_phra


    @staticmethod
    def get_thai_month(date, phase, day_count):
        if phase == "แรม" and day_count == 1:
            thai_month_map = {
                1: 3,  2: 4,  3: 5,  4: 6,  5: 7,  6: 8,
                7: 9,  8: 10, 9: 11, 10: 12, 11: 1, 12: 2
            }
        else:
            thai_month_map = {
                1: 2,  2: 3,  3: 4,  4: 5,  5: 6,  6: 7,
                7: 8,  8: 9,  9: 10, 10: 11, 11: 12, 12: 1
            }

        return thai_month_map.get(date.month, 1)  # คืนค่าตาม dictionary


# ทดสอบฟังก์ชัน
if __name__ == "__main__":
    today = datetime(2025,12,5) #datetime.today()
    lunar_date, is_wan_phra = ThaiLunarCalendar.get_lunar_date(today)

    print(f"วันที่ {today.strftime('%d-%m-%Y')} -> {lunar_date}, {'เป็นวันพระ' if is_wan_phra else 'ไม่ใช่วันพระ'}")
