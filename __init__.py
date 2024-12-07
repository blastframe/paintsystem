# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from bpy.utils import register_submodule_factory
import bpy
from . import auto_load
bl_info = {
    "name": "Paint System",
    "author": "Tawan Sunflower",
    "description": "",
    "blender": (4, 1, 0),
    "version": (1, 0, 0),
    "location": "View3D > Sidebar > Paint System",
    "warning": "",
    "category": "Node",
}


auto_load.init()


submodules = [
    # "properties",
    # "operators",
    "bruh",
    "layers",
    # "trail_handler"
]

register, unregister = register_submodule_factory(__name__, submodules)
