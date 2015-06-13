cpanimal - A CPAN-to-RPM compiling MACHINE
==========================================

We've all been there.  A new Perl project, to be deployed on your favorite
RPM-based OS stack.  So many dependencies.  And dependencies of
dependencies.  It's dependencies all the way down.

So you think about CPAN, if only for a fleeting minute.  It would be *so*
easy!  Just CPAN it and forget about the whole mess.

What if there was a better way?  Ideally, you want RPMs for all those dang
CPAN modules, but building packages is hard.  Then there's all those
dependencies.

cpanimal to the rescue!

It uses the MetaCPAN API to crawl CPAN, find all the dependencies, and then
builds concise little RPM packages for each module.  Lather, rinse, repeat.

Usage
-----

Itching to see what dependencies there are?

    $ cpanimal info My::Favorite::Module

Want to take a peek at the spec file before you commit?

    $ cpanimal spec My::Favorite::Module

Just need the archive?

    $ cpanimal source My::Favorite::Module

Curious about the dependency tree?

    $ cpanimal deptree Dancer

Ready to jump in with both feet?

    $ cpanimal build My::Favorite::Module

(or, my favorite)

    $ cpanimal A::Module Another::Module

That's it!


Contributing
------------

There's still some work to be done to make *cpanimal* really great.  If you
find it useful, and want to contribute back, take a look at the TODO file
and submit a Github Pull Request or three.

Happy Hacking!


Author
------

cpanimal was written by James Hunt, who was unhappy that David
Bishop hadn't already built all of CPAN into RPM packages.

License and Copyright
---------------------

cpanimal is Copyright (c) 2015 James Hunt <james@jameshunt.us>
Licensed under the GNU GPL, v3+ (see COPYING for details)
