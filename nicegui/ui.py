import os

from .elements.audio import Audio as audio
from .elements.badge import Badge as badge
from .elements.button import Button as button
from .elements.card import Card as card
from .elements.card import CardActions as card_actions
from .elements.card import CardSection as card_section
from .elements.chart import Chart as chart
from .elements.checkbox import Checkbox as checkbox
from .elements.color_input import ColorInput as color_input
from .elements.color_picker import ColorPicker as color_picker
from .elements.colors import Colors as colors
from .elements.column import Column as column
from .elements.dialog import Dialog as dialog
from .elements.expansion import Expansion as expansion
from .elements.html import Html as html
from .elements.icon import Icon as icon
from .elements.image import Image as image
from .elements.input import Input as input
from .elements.interactive_image import InteractiveImage as interactive_image
from .elements.joystick import Joystick as joystick
from .elements.keyboard import Keyboard as keyboard
from .elements.label import Label as label
from .elements.link import Link as link
from .elements.link import LinkTarget as link_target
from .elements.log import Log as log
from .elements.markdown import Markdown as markdown
from .elements.menu import Menu as menu
from .elements.menu import MenuItem as menu_item
from .elements.number import Number as number
from .elements.progress import CircularProgress as circular_progress
from .elements.progress import LinearProgress as linear_progress
from .elements.radio import Radio as radio
from .elements.row import Row as row
from .elements.scene import Scene as scene
from .elements.select import Select as select
from .elements.separator import Separator as separator
from .elements.slider import Slider as slider
from .elements.switch import Switch as switch
from .elements.table import Table as table
from .elements.toggle import Toggle as toggle
from .elements.tooltip import Tooltip as tooltip
from .elements.tree import Tree as tree
from .elements.upload import Upload as upload
from .elements.video import Video as video
from .functions.html import add_body_html, add_head_html
from .functions.javascript import run_javascript
from .functions.lifecycle import on_connect, on_disconnect, on_shutdown, on_startup, shutdown
from .functions.notify import notify
from .functions.open import open
from .functions.static_files import add_static_files
from .functions.timer import Timer as timer
from .functions.update import update
from .page import page
from .page_layout import Footer as footer
from .page_layout import Header as header
from .page_layout import LeftDrawer as left_drawer
from .page_layout import PageSticky as page_sticky
from .page_layout import RightDrawer as right_drawer
from .run import run
from .run_with import run_with

if os.environ.get('MATPLOTLIB', 'true').lower() == 'true':
    from .elements.line_plot import LinePlot as line_plot
    from .elements.plot import Plot as plot
