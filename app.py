class Timestamp:

	def __init__(self, raw_timestamp, description=''):
		self.raw_timestamp = raw_timestamp
		self.description = description

		words = raw_timestamp.split()
		self.user = words[0]
		self.terminal = words[1]
		self.address = words[2]
		self.day = words[3]
		self.month = words[4]
		self.date = words[5]
		self.startTime = words[6]
		self.endTime = words[8]
		self.duration = words[9].replace('(', '').replace(')', '')


	def setDescription(self, description):
		self.description = description



def build_timesheet(timestamps):
	html = '''
	<!DOCTYPE html>
	<html>
		<head>
			<title>GS-LSAMP Web Team Timesheet</title>
			<link rel="stylesheet" href="css/bulma.css">
		</head>

		<body>
			
			<section class="hero">
			  <div class="hero-body">
			    <div class="container">
			      <h1 class="title">
			        Md Islam
			      </h1>
			      <h2 class="subtitle">
			        lsamp@newark.gslsamp.rutgers.edu
			      </h2>
			    </div>
			  </div>
			</section>
			

			<section class="section">
				<div class="container">

					<table class="table">
					  	<thead>
					    	<tr>
					    		<th>Date</th>
					    		<th>Description</th>
					    		<th>Start</th>
					    		<th>End</th>
					    	</tr>
					    </thead>

				    <tbody>
    '''

	for timestamp in timestamps:
		html += '''
		<tr>
			<td>'''+timestamp.month+' '+timestamp.date+'''</td>
			<td>'''+timestamp.description+'''</td>
			<td>'''+timestamp.startTime+'''</td>
			<td>'''+timestamp.endTime+'''</td>
		</tr>
		'''

	html += '''
						</tbody>
					</table>
				</div>
				</section>
		</body>
	</html>
	'''

	return html


with open('current.timetable', 'r') as timefile:
	timetable = timefile.read()

timestamps = []

for line in timetable.split('\n'):
	timestamp = Timestamp(line)
	description = raw_input('What did you do '+timestamp.month+' '+timestamp.date+' between '+timestamp.startTime+' and '+timestamp.endTime+': ')
	timestamp.setDescription(description)
	timestamps.append(timestamp)

html = build_timesheet(timestamps)

with open('timesheet.html', 'w') as timesheet:
	timesheet.write(html)





	
