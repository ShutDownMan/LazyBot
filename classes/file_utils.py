# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import collections
import io
from os import remove, close, walk
from tempfile import mkstemp
from shutil import move

class File_Utils():

	Master = None

	def __init__(self, master):
		self.Master = master
		print "File_Utils module loaded!\n" + str(master)
	
	def get_file_array(self, file_path):
		file = io.open(file_path, "r")
		file_array = file.readlines()
		file.close()

		return file_array

	def get_config(self, config_type):
		file_array = None
		world = self.Master.current_world

		if config_type == "Troops Carrying Capacity":	# deprecated
			file_array = self.get_file_array(self.Master.Bot_Dir + '\\Game\\Configs\\Troops Carrying Capacity.txt')

		if config_type == "Troops Velocities":	# deprecated
			file_array = self.get_file_array(self.Master.Bot_Dir + '\\Game\\Configs\\Troops Velocities.txt')

		if config_type == "Barbarian Maps":
			file_array = self.get_file_array(self.Master.Bot_Dir + '\\Game\\Configs\\Barbarian Maps.txt')

		if config_type == "World Barbarian List":
			file_array = self.get_file_array(self.Master.Bot_Dir + '\\Game\\'+world+'\\Configs\\World Barbarians List.txt')

		if config_type == "Units Stats":
			file_dict = self.get_tree_log(self.Master.Bot_Dir + '\\Game\\Configs\\Units Stats.txt', 'Units Stats')
		#	print file_dict
			return file_dict['Units Stats']

		return file_array


	def get_village_status(self):
		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village
		log = self.get_file_array(self.Master.Bot_Dir + '\\Game\\Configs\\Villages Status.txt')
		status = {}
		index = [0]

		account_found = False
		world_found = False

		for index[0] in range(len(log)):
			splited_line = log[index[0]].split(':')

			if account in splited_line[0]:
				account_found = True
				continue

			if world in splited_line[0]:
				world_found = True
				continue

			if village in splited_line[0] and world_found and account_found:
				status = self.get_children(index, log)
				break

		self.Master.village_status = status

		return status


	def get_world_status(self):
		account = self.Master.current_account
		world = self.Master.current_world
		log = self.get_file_array(self.Master.Bot_Dir + '\\Game\\Configs\\Villages Status.txt')
		status = {}
		index = [0]

		account_found = False

		for index[0] in range(len(log)):
			if account in log[index[0]]:
				account_found = True

			if world in log[index[0]] and account_found:
				status = self.get_children(index, log)
				break

		self.Master.world_status = status

		return status


	def get_account_status(self):
		account = self.Master.current_account
		log = self.get_file_array(self.Master.Bot_Dir + '\\Game\\Configs\\Villages Status.txt')
		status = {}
		index = [0]

		for index[0] in range(len(log)):
			if account in log[index[0]]:
				status = self.get_children(index, log)
				break

		self.Master.world_status = status

		return status


	def get_attacks_log(self):
		account = self.Master.current_account
		world = self.Master.current_world
		log = self.get_file_array(self.Master.Bot_Dir + '\\Game\\'+account+'\\'+world+'\\Configs\\World Attacks List.txt')
		status = {}
		index = [0]

		for index[0] in range(len(log)):
			if village in log[index[0]]:
				status = collections.OrderedDict(self.get_children(index, log))
				break

		return status
		

	def get_tree_log(self, file_path, tree_parent='Tree'):
		log = self.get_file_array(file_path)
		status = {}
		index = [0]

		for index[0] in range(len(log)):
			if tree_parent in log[index[0]]:
				status.update({tree_parent:self.get_children(index, log)})
				break

		return status


	def get_closest_barbarians(self):
		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village
		log = self.get_file_array(self.Master.Bot_Dir + '\\Game\\'+account+'\\'+world+'\\Villages\\'+village+'\\Closest Barbarians.txt')
		barbs = []

		for i in range(len(log)):
			barbs.append(log[i].replace(' ', '').strip())

		return barbs


	def get_children(self, index, array):
		status = collections.OrderedDict()
		index[0] += 1
		try:
			while '}' not in array[index[0]]:

				line = array[index[0]]

				if (line.replace(' ','')).strip() != "":
					if ':' in line:
						splited_line = ((line.replace('\t','')).strip()).split(':')

						if '{' in line:
							status.update({str(splited_line[0]):self.get_children(index, array)})
						else:
							status.update({str(splited_line[0]):str(''.join(map(str, splited_line[1:]))).replace(' ','')})

						if '[' in line:
							status.update({str(splited_line[0]):self.get_list(index, array)})
					else:
						pass

				index[0] += 1

				if index[0] >= len(array):
					print 'Something went horribly wrong'
					break

		except Exception as ex:
			print ex
			print "Error getting status of line " + str(array[index[0]])

		return status


	def get_list(self, index, array):
		status_list = []
		index[0] += 1
		try:
			while ']' not in array[index[0]]:
				line = array[index[0]]

				if (line.replace(' ','')).strip() != "":
					status_list.append(str(line.strip()))

					index[0] += 1

		except:
			print "Error getting list on line " + str(array[index[0]])

		return status_list



	def update_village_status(self, status_to_change, new_value, *parents):
		account = self.Master.current_account
		world = self.Master.current_world
		file_path = self.Master.Bot_Dir + '\\Game\\Configs\\Villages Status.txt'
		hit = False

		found_parents = collections.OrderedDict()
		all_parents_found = False

		for parent in parents:
			found_parents.update({parent:False})

		#Create temp file
		fh, abs_path = mkstemp()
		with open(abs_path,'w') as new_file:
			with open(file_path) as old_file:
				for line in old_file:

					splited_line = line.split(':')
					# Check if parent in current line
					for parent in parents:
						if parent == splited_line[0].strip():
							found_parents[parent] = True
							break

					# Check if all parents found
					for parent, found in found_parents.items():
						all_parents_found = True
						if found == False:
							all_parents_found = False
							break

					if all_parents_found == False:
						new_file.write(line)
						continue

					if status_to_change in line and hit == False:
						hit = True
						value_to_change = splited_line[1]
						new_file.write(line.replace(value_to_change, new_value+'\n'))
					else:
						new_file.write(line)

					if line == '}':
						new_file.write(line)
						continue


		if hit == True:
			print 'Pattern Found!'

		close(fh)
		#Remove original file
		remove(file_path)
		#Move new file
		move(abs_path, file_path)

		self.get_village_status()

		return hit

		# bot.ufile.update_village_status('Spearman', "Paozin", self.Master.current_village, "Ideal Troop Division")

	def update_attack_status(self, barbarian, new_value):
		account = self.Master.current_account
		world = self.Master.current_world
		file_path = self.Master.Bot_Dir + '\\Game\\'+account+'\\'+world+'\\Configs\\Gobal Attacks List.txt'
		village_found = False
		hit = False

		#Create temp file
		fh, abs_path = mkstemp()
		with open(abs_path,'w') as new_file:
			with open(file_path) as old_file:
				for line in old_file:

					splited_line = line.split(':')
					# Check if parent in current line
					if village == splited_line[0].strip():
						village_found = True

					if village_found == False:
						new_file.write(line)
						continue

					if barbarian in line and hit == False:
						hit = True
						value_to_change = splited_line[1]
						new_file.write(line.replace(value_to_change, new_value+'\n'))
					else:
						new_file.write(line)

		if hit == True:
			print 'Pattern Found!'

		close(fh)
		#Remove original file
		remove(file_path)
		#Move new file
		move(abs_path, file_path)

		# bot.ufile.update_village_status('Spearman', "Paozin", self.Master.current_village, "Ideal Troop Division")



	def replaceline(self, file_path, pattern, subst):
		hit = False
		#Create temp file
		fh, abs_path = mkstemp()
		with open(abs_path,'w') as new_file:
			with open(file_path) as old_file:
				for line in old_file:
					if pattern in line and hit == False:
						hit = True
						new_file.write(line.replace(pattern, subst))
					else:
						new_file.write(line)

		if hit == True:
			print 'Pattern Found!'

		close(fh)
		#Remove original file
		remove(file_path)
		#Move new file
		move(abs_path, file_path)


	def removeline(self, file_path, lineToRemove):
		f = open(file_path,"r+")
		d = f.readlines()
		f.seek(0)
		hit = False
		for i in d:
			if i != lineToRemove:
				f.write(i)
			else:
				if hit == False:
					hit = True
				else:
					f.write(i)
		f.truncate()
		f.close()


	def sort_barbs(self, lim=60):
		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village

		f_barbVillages = self.get_file_array(self.Master.Bot_Dir + '\\Game\\'+account+'\\'+world+'\\Villages\\'+village+'\\Closest Barbarians.txt', "r")
		barbVillages = f_barbVillages.readlines()
		f_barbVillages.close()

		village_status = self.Master.world_status

		if village != '':
			vilSplit = village_status['Position']
			vilCoord = vilSplit[len(vilSplit)-1]
			vilCoord = vilCoord.split('|')
			vilCoord = [int(vilCoord[0]), int(vilCoord[1])]
		else:
			vilCoord = [500, 500]

		arr = {}
		a = 0

		for line in barbVillages:
			if line != '':
				a +=1
				hit = False
				splited = line.split('|')
				cord = (int(splited[0]), int(splited[1]))
				dist = self.Master.game.calculate_dist(vilCoord, cord)
				for k,v in arr.items():
					if k == cord:
						hit = True
				if hit == False:
					arr.update({cord:dist})

		sortedList = collections.OrderedDict(sorted(arr.iteritems(), key=lambda (k,v): (v,k)))

		f_barbVillages.seek(0)
		a = 0
		for i in sortedList:
			a += 1
			f_barbVillages.write((str(i[0]) +'|'+ str(i[1])) + '\n')
			if a == lim and village != '':
				break

		f_barbVillages.truncate()
		f_barbVillages.close()
		print "The village " + village + "'s barb list have been updated!"
