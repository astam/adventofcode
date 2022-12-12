module Model exposing (..)

import Array exposing (..)
import Debug exposing (..)
import Html exposing (..)
import Html.Events exposing (..)
import List exposing (..)
import Set exposing (..)


type alias Knots =
    { head : ( Int, Int )
    , tail : List ( Int, Int )
    , tailVisited : List ( Int, Int )
    , tailVisitedUniqueCount : Int
    }


type alias Move =
    ( String, Int )


startPoint : ( number, number )
startPoint =
    ( 0, 0 )


initKnots : Int -> Knots
initKnots tailCount =
    { head = startPoint
    , tail = List.repeat tailCount startPoint
    , tailVisited = [ startPoint ]
    , tailVisitedUniqueCount = 0
    }
