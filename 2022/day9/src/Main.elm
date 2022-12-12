module Main exposing (..)

import Array exposing (..)
import Debug exposing (..)
import Html exposing (..)
import Html.Events exposing (..)
import Input exposing (..)
import List exposing (..)
import Model exposing (..)
import Set exposing (..)


main : Html msg
main =
    div []
        [ Input.inputTest2
            |> decodePuzzleInput
            |> moveHead (initKnots 1)
            |> countUniqueVisited
            |> String.fromInt
            |> (++) "Score 1: "
            |> text
        , br [] []
        , Input.input
            |> decodePuzzleInput
            |> moveHead (initKnots 9)
            |> countUniqueVisited
            |> String.fromInt
            |> (++) "Score 2: "
            |> text
        ]


countUniqueVisited : Knots -> Int
countUniqueVisited knots =
    knots.tailVisited
        |> Set.fromList
        |> Set.size


moveHead : Knots -> List String -> Knots
moveHead knots moves =
    case moves of
        [] ->
            knots

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
                    moveTail newHead knots.tail

                newTailVisited =
                    (newTail
                        |> List.reverse
                        |> List.head
                        |> Maybe.withDefault ( 0, 0 )
                    )
                        :: knots.tailVisited
            in
            moveHead
                { knots
                    | head = newHead
                    , tail = newTail
                    , tailVisited = newTailVisited
                    , tailVisitedUniqueCount =
                        newTailVisited
                            |> Set.fromList
                            |> Set.size
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

        newTail =
            if abs diffX <= 1 && abs diffY <= 1 then
                tail

            else if abs diffX <= 1 && abs diffY == 2 then
                ( tailX + diffX, tailY + (diffY // 2) )

            else if abs diffX == 2 && abs diffY <= 1 then
                ( tailX + (diffX // 2), tailY + diffY )

            else if abs diffX == 2 && abs diffY == 2 then
                ( tailX + (diffX // 2), tailY + (diffY // 2) )

            else
                tail

        -- _ =
        --     Debug.log "head: " "-------------------"
        -- _ =
        --     Debug.log "head: " head
        -- _ =
        --     Debug.log "tail: " tail
        -- _ =
        --     Debug.log "diffX: " diffX
        -- _ =
        --     Debug.log "diffY: " diffY
        -- _ =
        --     Debug.log "newTail: " newTail
    in
    newTail
