from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodmt.native.structure import Structure as _molmodmt_Structure

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodmt_Structure : form_name,
    'molmodmt.Structure' : form_name
}


def select_with_mdtraj(item, selection):
    raise NotImplementedError(NotImplementedMessage)

def extract_atom_indices(item, atom_indices):
    raise NotImplementedError(NotImplementedMessage)

