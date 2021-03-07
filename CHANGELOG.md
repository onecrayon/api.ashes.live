# Changelog

The Ashes.live API uses [semantic versioning](https://semver.org/). Changes for major versions should be organized
by added, changed, deprecated, fixed, removed, and security in that order.

## Unreleased

(Forthcoming.)

## v2.0.0a2

### Added

* Authentication via JWT tokens
* Support for long-lived JWT tokens (up to 1 year)
* Ability to revoke JWT tokens in order to truly log out
* Account CRUD endpoints for managing a player's settings
* Basic public profile endpoint for players
* Deck CRUD endpoints for reading and writing both public and private decks
* Snapshot creation endpoint to create both private and public snapshots

### Changed

* Authentication response now includes active user information
* Updated dependencies to latest versions

### Fixed

* Search text now includes Phoenixborn name for unique cards

## v2.0.0a1 (2020-11-05)

Initial public release. Includes the card browsers for Reborn and legacy cards.
