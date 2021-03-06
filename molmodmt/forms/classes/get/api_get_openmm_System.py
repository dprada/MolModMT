
def getting(item, element='atom', indices=None, ids=None, **kwargs):

    result=[]
    args = [ii for ii in kwargs if kwargs[ii]]

    if element=='atom':

        for option in args:
            if option=='n_atoms':
                result.append(len(indices))
            elif option in ['atom_name', 'name']:
                atom=list(item.topology.atoms())
                atom_name=[atom[ii].name for ii in indices]
                del(atom)
                result.append(atom_name)
            elif option in ['atom_index', 'index']:
                result.append(indices)
            elif option in ['atom_id', 'id']:
                atom=list(item.topology.atoms())
                atom_type=[atom[ii].id for ii in indices]
                del(atom)
                result.append(atom_type)
            elif option in ['atom_type', 'type']:
                atom=list(item.topology.atoms())
                atom_type=[atom[ii].element.symbol for ii in indices]
                del(atom)
                result.append(atom_type)
            elif option=='n_residues':
                atom=list(item.topology.atoms())
                residue_indices = [atom[ii].residue.index for ii in indices]
                residue_indices = list(set(residue_indices))
                del(atom)
                result.append(len(residue_indices))
            elif option=='residue_name':
                residue_indices = getting(item, indices=indices, residue_index=True)
                residue=list(item.topology.residues())
                residue_names = [residue[ii].name for ii in residue_indices]
                del(residue, residue_indices)
                result.append(residue_names)
            elif option=='residue_index':
                atom=list(item.topology.atoms())
                residue_indices = [atom[ii].residue.index for ii in indices]
                del(atom)
                result.append(residue_indices)
            elif option=='residue_id':
                atom=list(item.topology.atoms())
                residue_ids = [atom[ii].residue.id for ii in indices]
                del(atom)
                result.append(residue_ids)
            elif option=='chain_index':
                atom=list(item.topology.atoms())
                chain_indices = [atom[ii].residue.chain.index for ii in indices]
                del(atom)
                result.append(chain_indices)
            elif option=='chain_id':
                atom=list(item.topology.atoms())
                chain_ids = [atom[ii].residue.chain.id for ii in indices]
                del(atom)
                result.append(chain_ids)
            elif option=='n_frames':
                raise Notimplementederror
            elif option=='n_chains':
                raise Notimplementederror
            elif option=='n_molecules':
                raise Notimplementederror
            elif option=='n_aminoacids':
                from molmodmt.topology import is_aminoacid
                residue_indices = getting(item, indices=indices, residue_index=True)
                residue_indices = list(set(residue_indices))
                residue_names = getting(item, element='residue', indices=residue_indices, residue_name=True)
                n_aminoacids=0
                for residue_name in residue_names:
                    if is_aminoacid(residue_name): n_aminoacids+=1
                del(residue_indices, residue_names)
                result.append(n_aminoacids)
            elif option=='n_nucleotides':
                from molmodmt.topology import is_nucleotide
                residue_indices = getting(item, indices=indices, residue_index=True)
                residue_indices = list(set(residue_indices))
                residue_names = getting(item, element='residue', indices=residue_indices, residue_name=True)
                n_nucleotides=0
                for residue_name in residue_names:
                    if is_nucleotide(residue_name): n_nucleotides+=1
                del(residue_indices, residue_names)
                result.append(n_nucleotides)
            elif option=='n_waters':
                from molmodmt.topology import is_water
                residue_indices = getting(item, indices=indices, residue_index=True)
                residue_indices = list(set(residue_indices))
                residue_names = getting(item, element='residue', indices=residue_indices, residue_name=True)
                n_waters=0
                for residue_name in residue_names:
                    if is_water(residue_name): n_waters+=1
                del(residue_indices, residue_names)
                result.append(n_waters)
            elif option=='n_ions':
                from molmodmt.topology import is_ion
                residue_indices = getting(item, indices=indices, residue_index=True)
                residue_indices = list(set(residue_indices))
                residue_names = getting(item, element='residue', indices=residue_indices, residue_name=True)
                n_ions=0
                for residue_name in residue_names:
                    if is_ion(residue_name): n_ions+=1
                del(residue_indices, residue_names)
                result.append(n_ions)
            elif option=='mass':
                from molmodmt import get_mass
                result.append(get_mass(item, indices))
            elif option=='net_mass':
                from molmodmt import get_net_mass
                result.append(get_net_mass(item, indices))
            elif option=='charge':
                from molmodmt import get_charge
                result.append(get_charge(item, indices))
            elif option=='net_charge':
                from molmodmt import get_net_charge
                result.append(get_net_charge(item, indices))
            elif option=='n_degrees_of_freedom':
                from molmodmt import get_degrees_of_freedom
                result.append(get_degrees_of_freedom(item))
            elif option=='bonded_atoms':
                raise NotImplementedError
            elif option=='bonds':
                raise NotImplementedError
            elif option=='graph':
                raise NotImplementedError
            elif option=='molecules':
                raise NotImplementedError
            elif option=='molecule_type':
                from molmodmt.topology import residue_name_to_molecule_type
                residue_names = getting(item, element='atom', indices=indices, residue_name=True)
                molecule_types = [residue_name_to_molecule_type(ii) for ii in residue_names]
                del(residue_names, residue_name_to_molecule_type)
                result.append(molecule_types)
            elif option=='coordinates':
                result.append(item.positions)
            else:
                raise NotImplementedError

    elif element=='residue':

        for option in args:
            if option=='n_atoms':
                raise NotImplementedError
            elif option=='atom_name':
                raise NotImplementedError
            elif option=='atom_type':
                raise NotImplementedError
            elif option=='n_residues':
                result.append(len(indices))
            elif option=='residue_name':
                residue=list(item.topology.residues())
                residue_names = [residue[ii].name for ii in indices]
                del(residue)
                result.append(residue_names)
            elif option=='residue_index':
                result.append(indices)
            elif option=='residue_id':
                residue=list(item.topology.residues())
                residue_ids = [residue[ii].id for ii in indices]
                del(residue)
                result.append(residue_ids)
            elif option=='chain_index':
                residue=list(item.topology.residues())
                chain_indices = [residue[ii].chain.index for ii in indices]
                del(residue)
                result.append(chain_indices)
            elif option=='chain_id':
                residue=list(item.topology.residues())
                chain_ids = [residue[ii].chain.id for ii in indices]
                del(residue)
                result.append(chain_ids)
            elif option=='n_frames':
                raise NotImplementedError
            elif option=='n_chains':
                raise NotImplementedError
            elif option=='n_molecules':
                raise NotImplementedError
            elif option=='n_aminoacids':
                raise NotImplementedError
            elif option=='n_nucleotides':
                raise NotImplementedError
            elif option=='n_waters':
                raise NotImplementedError
            elif option=='n_ions':
                raise NotImplementedError
            elif option=='masses':
                raise NotImplementedError
            elif option=='charge':
                raise NotImplementedError
            elif option=='bonded_atoms':
                raise NotImplementedError
            elif option=='bonds':
                raise NotImplementedError
            elif option=='graph':
                raise NotImplementedError
            elif option=='molecules':
                raise NotImplementedError
            elif option=='molecule_type':
                from molmodmt.topology import residue_name_to_molecule_type
                residue=list(item.topology.residues())
                residue_names = [residue[ii].name for ii in indices]
                molecule_types = [residue_name_to_molecule_type(ii) for ii in residue_names]
                del(residue, residue_names, residue_name_to_molecule_type)
                result.append(molecule_types)
            elif option=='coordinates':
                raise NotImplementedError
            else:
                raise NotImplementedError

    elif element=='molecule':
        raise NotImplementedError

    elif element=='chain':

        for option in args:
            if option=='n_atoms':
                raise NotImplementedError
            elif option=='atom_name':
                raise NotImplementedError
            elif option=='atom_type':
                raise NotImplementedError
            elif option=='n_residues':
                raise NotImplementedError
            elif option=='residue_name':
                raise NotImplementedError
            elif option=='residue_index':
                raise NotImplementedError
            elif option=='residue_id':
                raise NotImplementedError
            elif option=='chain_index':
                chain=list(item.topology.chains())
                chain_indices = [chain[ii].index for ii in indices]
                del(chain)
                result.append(chain_indices)
            elif option=='chain_id':
                chain=list(item.topology.chains())
                chain_ids = [chain[ii].id for ii in indices]
                del(chain)
                result.append(chain_ids)
            elif option=='n_frames':
                raise NotImplementedError
            elif option=='n_chains':
                result.append(len(indices))
            elif option=='n_molecules':
                raise NotImplementedError
            elif option=='n_aminoacids':
                raise NotImplementedError
            elif option=='n_nucleotides':
                raise NotImplementedError
            elif option=='n_waters':
                raise NotImplementedError
            elif option=='n_ions':
                raise NotImplementedError
            elif option=='masses':
                raise NotImplementedError
            elif option=='charge':
                raise NotImplementedError
            elif option=='bonded_atoms':
                raise NotImplementedError
            elif option=='bonds':
                raise NotImplementedError
            elif option=='graph':
                raise NotImplementedError
            elif option=='molecules':
                raise NotImplementedError
            elif option=='molecule_type':
                from molmodmt.topology import residue_name_to_molecule_type
                chain=list(item.topology.chains())
                molecule_types = []
                for ii in indices:
                    residue0 = list(chain[ii].residues())[0]
                    molecule_types.append(residue_name_to_molecule_type(residue0.name))
                del(chain, residue0)
                result.append(molecule_types)
            elif option=='coordinates':
                raise NotImplementedError
            else:
                raise NotImplementedError

    elif element=='trajectory':
        raise NotImplementedError

    elif element=='system':

        for option in args:
            if option=='n_atoms':
                result.append(len(indices))
            elif option=='charge':
                from molmodmt import get_net_charge
                result.append(get_net_charge(item, indices))
            elif option=='net_charge':
                from molmodmt import get_net_charge
                result.append(get_net_charge(item, indices))
            elif option=='n_degrees_of_freedom':
                from molmodmt import get_number_degrees_of_freedom
                result.append(get_degrees_of_freedom(item))
            else:
                raise NotImplementedError

    else:
        raise NotImplementedError


    if len(result)==1:
        return result[0]
    else:
        return result

