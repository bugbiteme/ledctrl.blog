import web
import RPi.GPIO as GPIO, time, os

DEBUG = False

GPIO.setmode(GPIO.BCM)

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class LightSwitch(object):
	
	def __init__(self, color):
		
		self.GREEN_LED = 24
		self.RED_LED = 23
		self.BLUE_LED = 18			
		self.LED = None	
		
		GPIO.setup(self.GREEN_LED, GPIO.OUT)
		GPIO.setup(self.RED_LED, GPIO.OUT)
		GPIO.setup(self.BLUE_LED, GPIO.OUT)
		
		if color:	
			if color in 'green':
				self.LED = self.GREEN_LED 
			elif color in 'blue':
				self.LED = self.BLUE_LED
			elif color in 'red':
				self.LED = self.RED_LED
			else:
				self.LED = None

		if DEBUG: print "LED COLOR: %r" % color
		
	def flip_switch(self):
		if self.LED == None:
			return None
			
		if DEBUG: print "LED on GPIO pin: %r" % self.LED
		
		led_status = GPIO.input(self.LED)
		if led_status == GPIO.LOW:
			GPIO.output(self.LED, True)
		else:
			GPIO.output(self.LED, False)
			
		return GPIO.input(self.LED)
		
	def get_light_statuses(self):
		return {'green': GPIO.input(self.GREEN_LED), 
		'blue': GPIO.input(self.BLUE_LED), 
		'red': GPIO.input(self.RED_LED)}
		
class Index(object):
    def GET(self):
        return render.hello_form(LightSwitch(None).get_light_statuses())

    def POST(self):
		
		form = web.input()
		light_switch = LightSwitch(form.led)
		light_switch.flip_switch()
		
		if DEBUG:
			print '-' * 20
			for color, status in light_switch.get_light_statuses().items():
				str_status = None
			
				if status == GPIO.LOW:
					str_status = "off"
				else:
					str_status = "on"
				
				print "The %s LED is %s" % (color, str_status)
			
			print '-' * 20
			
		return render.hello_form(light_switch.get_light_statuses())

if __name__ == "__main__":
	app.run()