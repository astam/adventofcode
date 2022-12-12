module Main exposing (..)

import Array exposing (..)
import Debug exposing (..)
import Html exposing (..)
import Html.Events exposing (..)
import List exposing (tail)
import Set exposing (..)


main : Html msg
main =
    div []
        [ input
            |> decodePuzzleInput
            |> moveHead1 initKnots1
            |> countUniqueVisited1
            |> String.fromInt
            |> (++) "Score 1: "
            |> text
        , br [] []
        , inputTest
            |> decodePuzzleInput
            |> moveHead2 initKnots2
            |> countUniqueVisited2
            |> String.fromInt
            |> (++) "Score 2: "
            |> text
        ]


type alias Knots1 =
    { head : ( Int, Int )
    , tail : ( Int, Int )
    , headVisited : List ( Int, Int )
    , tailVisited : List ( Int, Int )
    }


type alias Knots2 =
    { head : ( Int, Int )
    , tail : List ( Int, Int )
    , knot1 : ( Int, Int )
    , knot2 : ( Int, Int )
    , knot3 : ( Int, Int )
    , knot4 : ( Int, Int )
    , knot5 : ( Int, Int )
    , knot6 : ( Int, Int )
    , knot7 : ( Int, Int )
    , knot8 : ( Int, Int )
    , knot9 : ( Int, Int )
    , headVisited : List ( Int, Int )
    , tailVisited : List ( Int, Int )
    , lastVisited : List ( Int, Int )
    }


type alias Move =
    ( String, Int )


startPoint : ( number, number )
startPoint =
    ( 11, 5 )


initKnots1 : Knots1
initKnots1 =
    { head = startPoint
    , tail = startPoint
    , headVisited = []
    , tailVisited = []
    }


initKnots2 : Knots2
initKnots2 =
    { head = startPoint
    , tail = List.repeat 9 startPoint
    , knot1 = startPoint
    , knot2 = startPoint
    , knot3 = startPoint
    , knot4 = startPoint
    , knot5 = startPoint
    , knot6 = startPoint
    , knot7 = startPoint
    , knot8 = startPoint
    , knot9 = startPoint
    , headVisited = []
    , tailVisited = []
    , lastVisited = []
    }


decodePuzzleInput : String -> List String
decodePuzzleInput puzzleInput =
    puzzleInput
        |> String.split "\n"
        |> List.map (String.split " ")
        |> List.map
            (\x ->
                case x of
                    [ a, b ] ->
                        ( a, String.toInt b |> Maybe.withDefault 0 )

                    _ ->
                        ( "S", 0 )
            )
        |> extractMoves


countUniqueVisited1 : Knots1 -> Int
countUniqueVisited1 knots =
    knots.tailVisited
        |> Set.fromList
        |> Set.size


countUniqueVisited2 : Knots2 -> Int
countUniqueVisited2 knots =
    knots.tailVisited
        |> Set.fromList
        |> Set.size


extractMoves : List Move -> List String
extractMoves moves =
    case moves of
        x :: xs ->
            case x of
                ( a, b ) ->
                    List.repeat b a ++ extractMoves xs

        _ ->
            []


moveHead1 : Knots1 -> List String -> Knots1
moveHead1 knots moves =
    case moves of
        [] ->
            { knots
                | headVisited = List.append knots.headVisited [ knots.head ]
                , tailVisited = List.append knots.tailVisited [ knots.tail ]
            }

        x :: xs ->
            let
                newHead =
                    case x of
                        "R" ->
                            ( Tuple.first knots.head + 1, Tuple.second knots.head )

                        "L" ->
                            ( Tuple.first knots.head - 1, Tuple.second knots.head )

                        "U" ->
                            ( Tuple.first knots.head, Tuple.second knots.head + 1 )

                        "D" ->
                            ( Tuple.first knots.head, Tuple.second knots.head - 1 )

                        _ ->
                            knots.head

                newTail =
                    followHead newHead knots.tail
            in
            moveHead1
                { knots
                    | head = newHead
                    , tail = newTail
                    , headVisited = List.append knots.headVisited [ knots.head ]
                    , tailVisited = List.append knots.tailVisited [ knots.tail ]
                }
                xs


moveHead2 : Knots2 -> List String -> Knots2
moveHead2 knots moves =
    case moves of
        [] ->
            { knots
                | headVisited = knots.head :: knots.headVisited
                , tailVisited = knots.knot9 :: knots.tailVisited
            }

        x :: xs ->
            let
                newHead =
                    case x of
                        "R" ->
                            ( Tuple.first knots.head + 1, Tuple.second knots.head )

                        "L" ->
                            ( Tuple.first knots.head - 1, Tuple.second knots.head )

                        "U" ->
                            ( Tuple.first knots.head, Tuple.second knots.head + 1 )

                        "D" ->
                            ( Tuple.first knots.head, Tuple.second knots.head - 1 )

                        _ ->
                            knots.head

                newKnot1 =
                    followHead newHead knots.knot1

                newKnot2 =
                    followHead newKnot1 knots.knot2

                newKnot3 =
                    followHead newKnot2 knots.knot3

                newKnot4 =
                    followHead newKnot3 knots.knot4

                newKnot5 =
                    followHead newKnot4 knots.knot5

                newKnot6 =
                    followHead newKnot5 knots.knot6

                newKnot7 =
                    followHead newKnot6 knots.knot7

                newKnot8 =
                    followHead newKnot7 knots.knot8

                newKnot9 =
                    followHead newKnot8 knots.knot9

                newLastVisited =
                    [ newHead
                    , newKnot1
                    , newKnot2
                    , newKnot3
                    , newKnot4
                    , newKnot5
                    , newKnot6
                    , newKnot7
                    , newKnot8
                    , newKnot9
                    ]
            in
            moveHead2
                { knots
                    | head = newHead
                    , tail = moveTail newHead knots.tail
                    , knot1 = newKnot1
                    , knot2 = newKnot2
                    , knot3 = newKnot3
                    , knot4 = newKnot4
                    , knot5 = newKnot5
                    , knot6 = newKnot6
                    , knot7 = newKnot7
                    , knot8 = newKnot8
                    , knot9 = newKnot9
                    , headVisited = knots.head :: knots.headVisited
                    , tailVisited = knots.knot9 :: knots.tailVisited
                    , lastVisited = newLastVisited
                }
                xs


moveTail : ( Int, Int ) -> List ( Int, Int ) -> List ( Int, Int )
moveTail head tail =
    case tail of
        [] ->
            []

        x :: xs ->
            let
                newTail =
                    followHead head x
            in
            newTail :: moveTail newTail xs


followHead : ( Int, Int ) -> ( Int, Int ) -> ( Int, Int )
followHead head tail =
    let
        ( headX, headY ) =
            head

        ( tailX, tailY ) =
            tail

        diffX =
            headX - tailX

        diffY =
            headY - tailY
    in
    if abs diffX <= 1 && abs diffY <= 1 then
        tail

    else if abs diffX <= 1 && abs diffY == 2 then
        ( tailX + diffX, tailY + (diffY // 2) )

    else if abs diffX == 2 && abs diffY <= 1 then
        ( tailX + (diffX // 2), tailY + diffY )

    else
        tail


inputTest : String
inputTest =
    """R R 5
U 8
L 8
D 3"""


inputTest2 : String
inputTest2 =
    """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


input : String
input =
    """L 1
D 2
U 1
L 1
R 2
L 2
U 1
D 2
R 2
L 2
U 1
D 2
R 1
D 2
L 2
D 1
L 2
R 1
U 2
R 2
U 2
L 2
U 1
L 2
R 1
D 1
R 1
L 1
R 1
L 1
R 1
U 1
R 1
L 1
D 2
L 2
D 2
L 1
R 1
D 1
R 1
D 2
L 1
D 2
L 1
R 2
D 2
R 2
U 1
R 1
U 2
R 1
U 2
R 1
D 2
L 1
D 2
U 1
R 2
D 2
L 1
U 2
R 2
L 2
D 2
L 2
D 2
R 1
U 2
L 2
U 1
R 1
D 1
L 1
D 1
U 1
D 2
L 1
R 1
D 1
R 1
L 2
R 1
L 1
U 2
D 2
U 1
L 1
U 2
R 1
D 2
U 1
D 1
L 1
D 2
U 2
D 1
U 2
R 2
L 2
D 1
R 2
D 1
L 2
D 2
L 2
R 1
L 1
R 2
L 2
R 2
U 1
R 1
U 3
D 2
U 3
L 1
R 1
U 3
D 1
L 1
R 3
D 2
L 3
R 3
D 2
R 2
U 3
R 3
U 3
R 2
U 3
D 2
L 3
U 3
R 1
U 1
R 3
U 2
L 1
R 1
U 1
L 3
R 3
U 3
D 2
U 1
L 1
D 3
R 3
U 2
L 1
R 3
L 3
D 3
U 3
R 2
L 1
U 1
L 3
R 3
U 1
R 3
L 2
R 2
D 3
U 1
D 3
U 3
R 3
D 2
L 2
U 2
D 3
L 3
U 3
R 3
D 2
R 3
U 1
D 1
U 2
R 1
D 3
R 1
L 2
U 3
D 1
L 1
D 3
U 2
L 3
R 3
L 1
D 2
L 3
U 3
L 1
D 2
L 1
D 1
L 2
U 2
D 2
U 2
L 2
D 3
L 3
D 3
R 3
U 1
R 3
U 1
R 3
D 3
U 2
D 1
R 2
L 2
R 2
D 2
R 2
D 1
R 3
D 1
U 2
L 4
D 1
L 2
R 1
U 1
D 3
U 4
D 2
L 3
R 2
D 3
R 4
U 1
D 1
U 1
L 3
U 1
D 3
R 3
D 3
R 1
U 4
R 1
U 1
R 2
L 4
U 3
D 2
R 2
D 1
U 2
L 3
D 4
U 4
D 4
U 4
L 3
U 3
D 3
R 3
L 4
R 3
D 2
L 2
R 1
D 1
L 4
R 3
D 2
U 1
L 2
R 1
U 2
L 4
R 4
L 3
U 4
D 2
U 4
D 4
L 1
U 4
L 3
U 2
D 2
R 2
D 3
R 4
D 1
U 4
D 1
U 1
D 3
L 3
D 2
R 4
D 4
L 2
U 2
L 3
R 4
L 2
R 2
D 3
L 2
D 4
U 3
D 4
L 3
R 2
U 3
D 4
R 2
U 3
R 1
D 1
R 1
D 2
R 3
D 4
L 1
U 3
L 3
U 4
R 1
U 3
L 4
D 5
R 2
D 2
U 2
D 1
R 4
D 1
L 4
D 4
L 1
R 1
D 4
U 4
L 1
D 4
L 4
U 5
R 4
D 4
R 5
U 3
L 5
U 1
R 4
L 1
R 3
L 2
D 5
R 1
D 4
R 2
U 5
L 3
R 5
U 4
R 1
D 4
U 3
R 3
L 3
R 3
L 3
U 2
D 4
U 2
L 3
D 2
R 3
U 3
D 2
U 1
R 5
L 4
R 4
L 4
D 3
R 3
U 2
R 1
D 3
U 3
D 2
L 1
D 2
U 1
L 3
U 5
L 1
D 1
U 5
D 3
U 4
D 4
L 5
R 3
D 4
R 2
L 1
D 1
L 3
U 3
R 1
L 2
D 4
L 5
U 1
L 4
R 4
U 2
D 1
R 5
D 3
U 2
D 3
U 4
D 4
U 1
L 2
D 4
L 3
U 4
L 1
R 1
L 2
R 3
L 2
U 1
D 2
U 5
R 2
D 4
U 1
D 4
U 4
D 5
L 6
D 3
U 2
D 1
L 3
U 4
R 4
D 4
R 3
L 4
U 6
D 1
U 4
R 2
L 1
D 2
U 4
D 5
U 3
D 6
L 1
U 3
L 1
U 1
D 6
L 3
U 6
L 3
D 6
L 1
D 6
U 2
D 5
U 2
L 5
D 3
U 2
D 1
U 6
L 1
D 4
L 6
R 3
D 3
L 3
D 2
R 3
D 5
R 3
D 2
L 1
R 4
L 6
D 4
R 4
U 1
R 6
D 3
U 1
R 1
D 1
L 3
D 1
R 3
U 5
L 5
D 2
L 3
D 2
L 5
U 3
L 1
U 5
L 3
D 4
U 5
D 1
L 6
D 1
R 6
U 4
R 1
D 1
L 2
U 5
R 2
U 6
L 5
U 5
L 6
U 6
D 3
L 1
R 3
L 3
U 4
R 5
L 6
D 5
L 4
R 6
L 6
R 5
D 2
R 4
L 2
U 1
L 3
U 6
L 4
D 6
U 6
D 4
L 2
R 7
U 4
R 1
L 5
D 2
R 3
U 4
L 5
U 7
L 2
R 1
U 4
L 2
R 5
L 6
D 5
L 4
U 5
L 7
U 1
L 5
U 1
L 5
D 3
U 3
R 7
U 7
R 7
L 6
D 4
U 7
R 2
D 3
R 3
U 4
D 4
U 5
D 6
L 5
R 6
U 4
R 6
D 1
R 4
U 1
D 1
R 1
L 4
U 5
L 3
D 5
L 5
D 3
U 2
R 5
D 7
U 7
D 1
U 5
R 6
U 4
R 6
L 7
U 5
R 1
L 1
U 1
R 1
D 7
L 2
U 5
R 4
U 2
D 6
U 6
L 7
U 3
D 2
L 3
R 3
U 2
L 1
R 2
L 5
D 6
R 2
U 6
L 1
D 7
R 4
D 3
L 2
U 5
R 4
L 2
R 5
D 1
U 1
R 6
D 5
U 6
R 2
U 2
L 2
U 6
L 5
U 1
L 1
D 7
R 6
U 5
D 3
L 5
R 3
D 3
U 2
D 7
U 7
L 1
D 5
L 5
U 4
L 5
D 1
U 6
D 5
L 7
D 8
U 8
R 6
U 5
D 8
U 1
R 2
U 6
D 6
L 4
D 2
R 3
U 7
R 4
U 4
R 5
U 6
R 1
U 4
R 1
U 4
D 5
U 3
L 7
U 8
R 1
D 1
U 8
L 8
U 3
L 1
D 4
R 2
D 4
U 2
L 4
D 8
R 7
D 5
U 4
L 5
U 5
D 8
R 8
U 3
R 8
L 4
U 5
R 6
U 7
D 3
L 1
U 5
D 2
R 5
U 4
D 8
L 4
R 1
D 6
R 1
L 6
D 6
L 7
D 4
L 4
D 8
R 8
D 7
L 6
R 1
D 4
L 5
D 2
U 3
D 2
U 6
R 1
U 7
D 7
R 2
U 7
D 5
L 6
U 1
L 8
U 1
L 1
R 9
D 1
U 6
D 5
L 1
R 9
D 2
L 2
D 6
U 6
D 7
L 3
R 5
L 6
U 5
R 1
U 1
R 3
L 9
U 6
L 6
U 2
D 6
R 9
U 4
D 3
L 8
U 5
D 7
L 1
U 7
R 1
L 6
D 8
L 5
R 7
L 2
R 6
L 5
D 3
L 8
D 7
U 8
R 6
L 6
D 7
U 8
D 1
U 2
D 5
U 7
D 8
L 1
D 1
L 1
U 1
R 3
L 5
R 9
D 2
L 8
R 6
D 6
U 1
R 7
L 4
U 4
D 1
L 5
U 2
R 9
D 7
U 8
L 8
R 4
D 1
L 1
U 7
R 8
L 3
D 2
U 8
R 1
D 5
L 1
R 7
D 6
R 2
U 9
D 2
L 5
U 4
D 9
L 7
D 9
L 2
U 9
D 5
L 7
D 6
U 5
D 9
R 3
U 8
L 7
U 1
L 3
U 3
D 1
L 6
R 9
U 2
L 7
R 9
U 5
R 2
L 3
R 4
D 9
L 4
R 9
U 4
L 10
R 9
D 9
U 10
L 2
R 4
U 4
R 9
D 2
R 1
L 4
R 7
D 3
L 6
U 1
L 9
D 6
U 10
D 1
R 10
D 9
L 6
D 10
U 3
R 10
L 8
U 9
D 1
L 1
D 10
L 1
D 5
L 9
U 3
L 4
U 4
D 1
U 3
R 7
L 3
R 3
L 3
R 8
D 9
R 4
L 6
D 7
R 10
U 6
R 2
D 2
L 3
R 9
D 9
U 7
D 2
R 6
U 10
R 8
U 5
R 5
U 10
R 6
U 7
L 7
U 7
D 4
L 9
U 2
R 7
L 8
R 4
L 1
U 9
R 8
D 4
R 5
D 4
L 1
D 10
R 8
D 10
U 9
D 3
R 1
U 10
R 1
D 10
R 1
L 6
D 3
U 8
R 4
U 9
D 8
U 3
D 2
R 3
L 5
U 4
L 3
R 4
D 6
L 9
R 1
D 9
R 2
D 11
R 8
D 5
R 8
L 2
D 2
L 7
U 11
D 10
L 6
R 2
U 9
L 10
D 4
L 5
R 7
D 4
L 1
U 3
L 9
D 7
R 4
D 10
L 5
U 9
L 10
D 5
L 11
R 11
U 8
R 11
U 2
R 7
L 10
R 2
D 8
L 2
D 8
R 11
L 6
R 3
L 2
U 2
R 2
U 3
D 3
U 5
L 8
U 9
R 10
D 1
U 4
D 8
R 3
D 11
R 4
D 4
R 7
U 6
L 11
U 11
D 8
L 5
R 2
L 11
U 7
D 5
U 5
D 9
L 2
U 3
R 10
U 1
R 1
L 11
D 3
L 5
R 2
L 10
R 4
L 1
U 1
L 4
R 5
U 2
D 6
R 11
U 8
D 5
R 5
D 3
L 2
U 7
D 10
L 11
D 10
U 11
R 8
L 2
D 9
R 9
L 11
R 10
U 3
R 4
L 5
R 12
U 5
D 5
L 6
D 11
R 8
D 12
U 6
L 10
R 9
U 1
L 12
D 1
R 8
U 9
D 9
R 6
D 3
L 1
R 3
L 8
R 6
U 12
L 1
U 8
D 7
U 5
D 12
L 4
R 11
U 9
D 12
R 8
D 2
R 7
U 8
R 10
U 3
R 4
D 4
U 9
R 7
L 9
R 7
U 8
L 9
U 6
R 4
L 11
D 11
R 6
U 2
D 1
R 2
L 2
D 11
R 5
U 1
R 1
D 3
U 2
L 3
U 12
R 10
U 12
R 9
D 11
U 9
L 2
R 7
U 5
R 7
U 9
R 3
D 4
L 9
D 4
R 12
L 3
U 12
L 9
U 3
L 11
R 7
U 11
D 2
L 11
R 2
L 12
U 10
L 6
R 8
D 6
R 12
L 7
R 4
U 5
D 10
R 8
L 11
D 4
U 1
R 9
U 12
D 3
L 10
R 11
U 1
L 5
U 11
L 7
U 1
D 13
U 10
L 12
U 9
D 8
L 5
R 4
L 1
R 2
L 7
D 1
L 11
U 9
R 5
D 12
L 4
U 7
L 6
R 7
U 1
L 7
U 2
D 4
R 4
D 7
L 3
D 9
U 3
D 3
U 12
R 2
L 12
R 9
L 8
D 10
U 1
R 11
L 13
U 1
D 3
U 12
L 3
R 7
L 7
D 7
U 7
D 7
U 10
D 1
L 7
D 11
R 3
D 6
R 9
D 5
U 12
D 6
R 8
D 3
R 7
L 6
D 10
U 8
R 9
D 4
R 9
D 2
U 4
R 4
U 7
L 12
R 2
D 10
U 13
R 12
L 12
D 1
R 11
L 2
U 13
L 12
D 7
L 2
U 4
L 4
D 8
L 9
R 3
D 4
L 9
U 9
L 9
R 10
L 4
R 4
U 10
L 11
D 8
U 8
L 13
R 1
L 8
U 13
L 9
U 1
R 13
U 7
L 3
R 8
L 1
D 5
R 7
U 8
D 5
L 12
R 11
U 11
D 10
U 5
R 6
D 11
R 1
D 1
R 9
L 8
D 4
L 11
U 9
D 4
U 3
D 13
U 13
L 6
D 6
R 11
L 9
U 3
R 7
D 9
R 5
L 9
D 14
R 8
L 14
R 6
L 6
U 6
R 7
L 11
R 1
L 6
D 10
R 1
D 14
R 12
U 4
R 2
L 9
R 14
L 3
D 9
U 10
R 11
L 5
R 14
U 3
D 8
R 9
L 13
U 4
L 2
R 4
D 6
L 13
D 4
R 2
L 2
D 10
L 10
R 4
D 2
R 2
U 6
D 7
U 12
R 5
U 13
L 6
U 12
L 3
D 11
R 3
L 7
U 11
D 4
L 13
U 14
R 10
D 12
U 2
L 1
U 12
D 6
U 2
R 12
L 3
D 9
U 9
R 14
L 12
R 5
L 11
R 11
L 5
R 2
L 4
D 8
U 3
R 4
D 12
R 10
L 10
D 10
U 10
R 9
L 14
R 3
L 1
D 1
R 15
D 15
R 12
L 15
D 12
L 10
R 3
U 14
D 4
U 7
R 11
L 10
U 4
D 15
L 3
U 1
R 2
L 15
U 6
L 6
D 3
L 14
D 12
U 1
L 15
R 13
U 7
D 6
R 11
U 7
L 2
D 11
L 1
R 7
D 1
L 4
R 11
U 5
L 4
R 13
U 1
D 4
L 6
R 10
L 15
U 7
D 9
L 10
R 8
U 10
D 8
L 14
D 15
R 14
U 10
D 4
U 6
D 2
R 6
L 6
D 4
U 12
L 3
R 6
U 9
R 3
U 11
R 3
U 15
D 1
U 2
D 3
U 11
L 3
U 2
L 14
D 3
R 9
D 5
L 10
U 7
L 6
D 8
L 8
U 8
L 14
R 9
L 14
U 10
L 8
U 5
L 2
U 4
D 5
R 2
L 1
U 14
R 3
L 4
U 9
D 7
U 14
D 11
R 9
U 5
R 8
L 5
U 3
D 8
R 8
L 11
R 7
L 3
D 16
L 11
U 7
D 6
R 5
L 4
U 9
L 12
R 9
L 10
D 13
L 3
D 13
U 6
R 14
U 2
L 5
R 4
L 15
U 9
D 5
L 6
R 7
U 10
L 3
D 5
U 8
D 12
L 11
U 14
D 12
U 2
D 9
U 11
D 5
L 5
R 10
L 14
U 1
R 8
D 5
R 6
U 6
L 3
U 11
L 8
R 3
U 5
L 1
R 16
D 10
U 12
R 11
D 2
U 4
D 15
U 16
D 2
L 9
R 10
L 3
U 8
R 13
U 11
D 12
U 15
D 1
L 14
R 3
U 13
D 7
R 15
L 3
R 1
U 7
R 6
D 12
L 2
R 13
D 3
R 6
D 10
U 2
R 4
D 12
L 7
R 7
L 8
R 14
L 15
D 8
L 6
U 14
L 16
U 10
D 7
R 6
D 12
R 16
U 11
R 2
U 10
L 1
R 6
U 14
D 13
U 7
L 10
D 4
L 7
R 11
U 17
D 6
U 6
R 6
U 12
L 16
U 5
R 15
L 17
D 13
U 12
L 1
D 7
L 13
R 7
U 2
L 5
U 12
R 10
U 7
R 11
U 17
D 15
U 15
L 10
D 3
L 15
U 8
R 8
D 10
L 9
U 6
R 9
L 1
U 5
R 6
L 11
D 17
L 7
U 3
D 17
R 17
U 8
L 15
R 3
D 2
U 17
L 1
R 13
U 13
L 10
R 2
D 12
L 12
R 13
L 14
R 16
D 12
R 4
U 14
L 15
R 10
D 7
R 12
U 6
L 8
U 7
R 1
D 3
R 3
L 11
D 2
R 15
U 17
L 13
U 17
D 4
U 11
L 17
D 12
R 3
L 12
U 8
D 2
L 14
U 16
D 6
U 7
L 12
R 17
L 7
D 1
L 16
D 16
R 17
D 5
U 16
D 2
L 13
U 9
D 13
R 3
U 1
D 12
R 4
D 11
L 8
D 8
R 13
D 16
R 1
D 10
R 18
U 6
D 4
U 17
R 12
L 14
U 5
L 15
U 18
R 4
D 17
L 4
R 18
U 18
D 4
L 1
U 4
L 2
U 17
R 16
L 7
U 10
R 11
U 9
R 11
L 16
U 3
R 3
L 18
U 8
R 1
U 1
L 5
U 5
D 7
L 1
R 2
U 16
R 17
D 4
U 16
L 12
R 3
L 16
D 5
U 5
R 18
L 7
U 1
L 7
U 16
R 14
L 4
R 13
L 3
U 4
L 11
U 3
L 12
U 16
L 14
U 3
L 9
R 18
D 8
L 15
R 10
D 2
L 13
D 11
U 4
L 13
D 7
L 12
U 7
D 17
U 9
D 5
L 10
R 2
D 7
L 14
U 10
D 17
L 3
R 17
U 16
D 13
R 13
U 14
R 9
L 3
U 14
L 7
U 4
D 1
R 18
U 11
D 9
U 8
R 15
L 5
D 9
L 2
D 18
U 12
D 3
U 14
D 9
U 13
R 16
U 8
R 16
U 4
L 8
D 14
R 15
D 6
R 17
U 6
D 1
L 2
U 9
D 15
L 7
D 3
R 1
L 1
R 17
D 12
R 19
U 4
R 19
L 2
D 17
U 11
D 1
L 9
R 18
L 7
D 13
U 6
D 16
L 6
R 13
U 12
R 1
L 2
U 8
L 16
R 10
D 15
R 5
L 1
U 5
R 18
U 1
R 4
U 14
R 3
L 4
U 13
D 14
L 10
D 7
U 3
R 17
L 19
R 1
D 12
L 9
U 19
D 19
L 5
R 10
L 14
U 15
D 19
U 18
D 14
R 11
U 8
R 2
U 16
L 17
D 6
L 1
D 10
R 18
U 5
R 14
U 10
D 6
L 17
D 6
U 7
R 14
L 1
U 3
D 3
R 18
D 1
L 6
D 18
L 2
R 10
L 9
R 10
L 14
R 15
U 10"""
