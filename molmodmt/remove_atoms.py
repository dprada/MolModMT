# =======================
# BUH
# =======================


"""
Remove Atoms
==============

Methods to remove atoms from a molecular model.

"""


def remove (item, selection=None, syntaxis='mdtraj'):
    """remove(item, selection=None, syntaxis='mdtraj')

    Remove a set of atoms from the molecular model

    Parameters
    ----------
    item : molecular model
        Molecular model in any form to be operated by the method.
    selection : str, int, list, tuple or numpy array
        Selection sentence or atoms indices list.
    syntaxis : str (default "mdtraj")
        Name of the selection syntaxis used: "mdtraj" or "amber".

    Returns
    -------
    item : molecular model
        The result is a new molecular model with the same form as the input item.

    Examples
    --------
    Remove chains 0 and 1 from the pdb: 1B3T.
    >>> import molmodmt as m3t
    >>> system = m3t.load('pdb:1B3T')
    Check the number of chains
    >>> m3t.get(system, n_chains=True)
    8
    Remove chains 0 and 1
    >>> new_system = m3t.remove(system, 'chainid 0 1')
    Check the number of chains of the new molecular model
    >>> m3t.get(new_system, n_chains=True)
    6

    See Also
    --------
    molmodmt.selection

    Notes
    -----
    There is a special function to remove solvent atoms: molmodmt.remove_solvent
    """

    from .multitool import select as _select
    from .multitool import extract as _extract

    atoms_list_to_be_removed = _select(item, selection, syntaxis=syntaxis)
    atoms_list_all = _select(item, 'all', 'mdtraj')
    atoms_list_survive = list(set(atoms_list_all) - set(atoms_list_to_be_removed))

    return _extract(item, atoms_list_survive)


def remove_solvent (item, ions=False, include_selection=None, exclude_selection=None,
                   syntaxis='mdtraj'):

    from .multitool import select as _select
    from .utils.types import water_residues as _water_residues
    from .utils.types import ion_residues as _ion_residues

    atoms_list_to_be_removed = []
    atoms_list_water = []
    atoms_list_ions = []
    atoms_list_included = []
    atoms_list_excluded = []

    atoms_list_water = _select(item, 'resname '+' '.join([str(ii) for ii in _water_residues]),
                               syntaxis='mdtraj')

    if ions:
        atoms_list_ions = _select(item, 'resname '+' '.join([str(ii) for ii in _ion_residues]),
                                  syntaxis='mdtraj')

    if include_selection is not None:
        atoms_list_included = _select(item, include_selection, syntaxis=syntaxis)

    if exclude_selection is not None:
        atoms_list_excluded = _select(item, exclude_selection, syntaxis=syntaxis)

    atoms_list_to_be_removed = list(set(atoms_list_water) | set(atoms_list_ions) | set(atoms_list_included))
    atoms_list_to_be_removed = list(set(atoms_list_to_be_removed) - set(atoms_list_excluded))

    return _extract(item, atoms_list_to_be_removed)