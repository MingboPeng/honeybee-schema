"""Boundary condition schemas."""
from pydantic import BaseModel, Field, constr
from typing import List, Union


class Outdoors(BaseModel):

    type: constr(regex='^Outdoors$') = 'Outdoors'

    sun_exposure: bool = Field(
        True,
        description='A boolean noting whether the boundary is exposed to sun.'
    )

    wind_exposure: bool = Field(
        True,
        description='A boolean noting whether the boundary is exposed to wind.'
    )

    view_factor: Union[str, float] = Field(
        'autocalculate',
        ge=0,
        le=1,
        description='A number for the view factor to the ground. This can also be '
            'the word "autocalculate" to have the view factor automatically calculated.'
    )

class Surface(BaseModel):

    type: constr(regex='^Surface$') = 'Surface'

    boundary_condition_objects: List[str] = Field(
        ...,
        min_tems=2,
        max_items=3,
        description='A list of up to 3 object names that are adjacent to this one. '
            'The first object is always the one that is immediately adjacet and is of '
            'the same object type (Face, Aperture, Door). When this boundary condition '
            'is applied to a Face, the second object in the tuple will be the parent '
            'Room of the adjacent object. When the boundary condition is applied to a '
            'sub-face (Door or Aperture), the second object will be the parent Face '
            'of the adjacent sub-face and the third object will be the parent Room '
            'of the adjacent sub-face.'
    )


class Ground(BaseModel):

    type: constr(regex='^Ground$') = 'Ground'


class Adiabatic(BaseModel):

    type: constr(regex='^Adiabatic$') = 'Adiabatic'
