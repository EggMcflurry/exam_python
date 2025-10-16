import psutil 
import time

def monitoring_cpu(interval =0.5):
    """övervakar CPU-andvändning"""
    try: 
        print("startar övervakning . tryck ctrl+ c för att avsluta")
        while True: 
            cpu_percent = psutil.cpu_percent(interval = interval)
            
            print(f"CPU-användning:{cpu_percent}%")
    except KeyboardInterrupt:
     print("\navslutad")
if __name__=="__main__":
   
    monitoring_cpu()

            