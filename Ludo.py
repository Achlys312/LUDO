                                                        # Ludo game Integrated With AI #
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint, choice

class Ludo:
    def __init__(self, root,six_side_block,five_side_block,four_side_block,three_side_block,two_side_block,one_side_block):
        self.window = root
        # Make canvas
        self.make_canvas = Canvas(self.window, bg="#141414", width=800, height=630)
        self.make_canvas.pack(fill=BOTH,expand=1)

        # Make some containers to store data
        self.made_red_coin = []
        self.made_green_coin = []
        self.made_yellow_coin = []
        self.made_sky_blue_coin = []

        self.red_number_label = []
        self.green_number_label = []
        self.yellow_number_label = []
        self.sky_blue_number_label = []

        self.block_value_predict = []
        self.total_people_play = []

        # Ludo block all side image store
        self.block_number_side = [one_side_block, two_side_block, three_side_block, four_side_block, five_side_block, six_side_block]
        
        # Use for store specific position of all coins
        self.red_coord_store = [-1, -1, -1, -1]
        self.green_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.sky_blue_coord_store = [-1, -1, -1, -1]

        self.red_coin_position = [0, 1, 2, 3]
        self.green_coin_position = [0, 1, 2, 3]
        self.yellow_coin_position = [0, 1, 2, 3]
        self.sky_blue_coin_position = [0, 1, 2, 3]

        for index in range(len(self.red_coin_position)):# Specific coin position set to -1 by default
            self.red_coin_position[index] = -1
            self.green_coin_position[index] = -1
            self.yellow_coin_position[index] = -1
            self.sky_blue_coin_position[index] = -1