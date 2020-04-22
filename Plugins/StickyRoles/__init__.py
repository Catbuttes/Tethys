from Plugins.StickyRoles import StickyRoles
import Tethys


def setup(bot: Tethys):
    bot.add_cog(StickyRoles.StickyRoles(bot))
