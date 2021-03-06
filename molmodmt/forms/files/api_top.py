from os.path import basename as _basename
from molmodmt.utils.exceptions import *

form_name=_basename(__file__).split('.')[0].split('_')[-1]

is_form = {
    'top': form_name
    }


def to_parmed(item):
    return to_parmed_GromacsTopologyFile(item)

def to_parmed_Structure(item):
    return to_parmed_GromacsTopologyFile(item)

def to_parmed_GromacsTopologyFile(item):

    from parmed.gromacs import GromacsTopologyFile as _parmed_from_gromacs
    tmp_molmod_Structure=_parmed_from_gromacs(item)
    return tmp_molmod_Structure

def to_molmodmt_Structure(item):

    from molmodmt.native.io_structure import _from_gromacs_Topology
    return _from_gromacs_Topology(item)

def to_top(item,filename=None,selection=None,syntaxis='mdtraj'):
    from molmodmt import extract as _extract
    tmp_item = to_parmed_GromacsTopologyFile(item)
    if selection is not None:
        tmp_item = _extract(tmp_item,selection=selection,syntaxis=syntaxis)
    tmp_item.save(filename)
    pass
