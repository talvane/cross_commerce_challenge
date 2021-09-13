from fastapi import APIRouter, HTTPException

from api.services import ApiNumber
from api.utils.array_order import quickSort


router = APIRouter(
    prefix='/numbers',
    tags=['numbers']
)


@router.get(
    '/',
    responses={
        200: {
            'content': {
                'application/json': {
                    'numbers': []
                }
            },
            'description': 'Return the ordered numbers.'
        }
    }
)
async def get_numbers():
    apinumber = ApiNumber()
    apinumber.get_numbers()
    array_numbers = apinumber.array_numbers

    if len(array_numbers) > 0:
        quickSort(array_numbers)
        return array_numbers
    else:
        raise HTTPException(status_code=400)
