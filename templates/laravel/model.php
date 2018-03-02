<?php

namespace App\Models\;

use Illuminate\Database\Eloquent\Model;


class [--name--] extends Model
{


    protected $table = '[--table_name--]';

    protected $fillable = [
        [--fillable_fields--]
    ];

    protected $primaryKey = '[--primary_key--]';

    protected $foreignKey = [
        [--foreign_keys--]
    ];

    public $timestamps = false;

    [--add_methods--]
    
}
