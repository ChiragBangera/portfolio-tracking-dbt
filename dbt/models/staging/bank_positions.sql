select *
from {{ source('abc_bank', 'ABC_BANK_POSITIONS')}}
